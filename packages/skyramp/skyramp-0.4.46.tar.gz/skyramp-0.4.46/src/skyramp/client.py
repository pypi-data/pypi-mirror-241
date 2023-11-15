"""
Defines a Skyramp client, which can be used to interact with a cluster.
"""

import ctypes
import json
from typing import List, Union
import yaml

from skyramp.utils import _library, _call_function, add_unique_items
from skyramp.scenario import _Scenario
from skyramp.endpoint import _Endpoint
from skyramp.test_description import _TestDescription
from skyramp.test_request import _Request
from skyramp.utils import SKYRAMP_YAML_VERSION

class _Client:
    """
    Skyramp client object which can be used to interact with a cluster.
    """

    def __init__(
        self,
        kubeconfig_path: str = "",
        cluster_name: str = "",
        context: str = "",
    ) -> None:
        """
        Initializes a Skyramp Client.

        kubeconfig_path: The filesystem path of a kubeconfig
        cluster_name: The name of the cluster.
        context: The Kubernetes context within a kubeconfig
        """
        self.kubeconfig_path = kubeconfig_path
        self.cluster_name = cluster_name
        self.context = context
        self.project_path = ""
        self._namespace_set = set()
        self.global_headers = {}

    def apply_local(self) -> None:
        """
        Creates a local cluster.
        """
        apply_local_function = _library.applyLocalWrapper
        argtypes = []
        restype = ctypes.c_char_p

        _call_function(apply_local_function, argtypes, restype, [])

        self.kubeconfig_path = self._get_kubeconfig_path()
        if not self.kubeconfig_path:
            raise Exception("no kubeconfig found")

    def remove_local(self) -> None:
        """
        Removes a local cluster.
        """
        func = _library.removeLocalWrapper
        argtypes = []
        restype = ctypes.c_char_p

        _call_function(func, argtypes, restype, [])

    def add_kubeconfig(
        self,
        context: str,
        cluster_name: str,
        kubeconfig_path: str,
    ) -> None:
        """
        Adds a preexisting Kubeconfig file to Skyramp.

        context: The kubeconfig context to use
        cluster_name: Name of the cluster
        kubeconfig_path: filepath of the kubeconfig
        """
        func = _library.addKubeconfigWrapper
        argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
        restype = ctypes.c_char_p

        _call_function(
            func,
            argtypes,
            restype,
            [
                context.encode(),
                cluster_name.encode(),
                kubeconfig_path.encode(),
            ],
        )

        self.kubeconfig_path = kubeconfig_path

    def remove_cluster(self, cluster_name: str) -> None:
        """
        Removes a cluster, corresponding to the name, from Skyramp
        """
        func = _library.removeClusterFromConfigWrapper
        argtypes = [ctypes.c_char_p]
        restype = ctypes.c_char_p

        _call_function(func, argtypes, restype, [cluster_name.encode()])

    def deploy_skyramp_worker(
        self, namespace: str, worker_image: str='', local_image: bool=False
    ) -> None:
        """
        Installs a Skyramp worker onto a cluster if one is registered with Skyramp
        """
        if not self.kubeconfig_path:
            raise Exception("no cluster to deploy worker to")

        func = _library.deploySkyrampWorkerWrapper
        argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_bool]
        restype = ctypes.c_char_p

        _call_function(
            func,
            argtypes,
            restype,
            [namespace.encode(), worker_image.encode(), local_image],
        )

        self._namespace_set.add(namespace)

    def delete_skyramp_worker(self, namespace: str) -> None:
        """
        Removes the Skyramp worker, if a Skyramp worker is installed on a registered Skyramp cluster
        """
        if not self.kubeconfig_path:
            raise Exception("no cluster to delete worker from")

        if namespace not in self._namespace_set:
            raise Exception(f"no worker to delete from {namespace} namespace")

        func = _library.deleteSkyrampWorkerWrapper
        argtypes = [ctypes.c_char_p]
        restype = ctypes.c_char_p

        _call_function(func, argtypes, restype, [namespace.encode()])

        self._namespace_set.remove(namespace)

    def mocker_apply(self, namespace: str, address: str, endpoint) -> None:
        """
        Applies a configuration to mocker.
        namespace: The namespace where Mocker resides
        address: The address of Mocker
        endpoint: The Skyramp enpdoint object
        """
        yaml_string = yaml.dump(endpoint.mock_description)

        func = _library.applyMockDescriptionWrapper
        argtypes = [
            ctypes.c_char_p,
            ctypes.c_char_p,
            ctypes.c_char_p,
        ]

        _call_function(
            func,
            argtypes,
            ctypes.c_char_p,
            [
                namespace.encode(),
                address.encode(),
                yaml_string.encode(),
            ],
        )

    def _get_kubeconfig_path(self) -> str:
        func = _library.getKubeConfigPath
        argtypes = []
        restype = ctypes.c_char_p

        return _call_function(func, argtypes, restype, [], True)

    def set_project_directory(self, path: str) -> None:
        """
        Sets the project directory for the client.
        """
        self.project_path = path
        func = _library.setProjectDirectoryWrapper
        argtypes = [ctypes.c_char_p]
        restype = ctypes.c_char_p

        return _call_function(func, argtypes, restype, [path.encode()])

    def load_endpoint(self, name: str) -> _Endpoint:
        """
        Loads an endpoint from a file.
        """
        if not self.project_path:
            raise Exception("project path not set")
        func = _library.getEndpointFromProjectWrapper
        argtypes = [ctypes.c_char_p, ctypes.c_char_p]
        restype = ctypes.c_char_p

        endpoint_data = _call_function(
            func,
            argtypes,
            restype,
            [
                name.encode(),
                self.project_path.encode(),
            ],
            True,
        )
        if not endpoint_data:
            raise Exception(f"endpoint {name} not found")
        try:
            endpoint = json.loads(endpoint_data)
        except json.JSONDecodeError:
            raise ValueError(f"Endpoint data for {name} is not valid JSON")
        return _Endpoint(json.dumps(endpoint))

    def tester_start_v1(
            self,
            scenario: Union[_Scenario, List[_Scenario]],
            global_headers: map=None,
            namespace: str='',
            address: str='',blocked=False) -> str:
        """
        Runs testers. If namespace is provided, connects with the worker instance running
        on the specified namespace in the registered Kubernetes cluster. If address is provided,
        connects to the worker directly using the network address.
        namespace: The namespace where mocker resides
        address: The address to reach mocker
        scenario: Scenario object for the test to run
        """
        if scenario is None:
            raise Exception("no scenario provided")

        if isinstance(scenario, list):
            test_description = _TestDescription(
                version= SKYRAMP_YAML_VERSION,
                test= {
                    "testPattern": [],
                },
                scenarios=[],
                services=[],
                requests=[],
                endpoints=[],
            )
            for test_scenario in scenario:
                test_scenario.set_global_headers(global_headers)
                test_desc = self.get_test_description_v1(test_scenario)
                add_unique_items(test_description.services, test_desc.services)
                add_unique_items(test_description.endpoints, test_desc.endpoints)
                add_unique_items(test_description.requests, test_desc.requests)
                add_unique_items(test_description.scenarios, test_desc.scenarios)
                # combine all the test patterns into one test_description
                test_pattern = test_desc.test["testPattern"]
                add_unique_items(test_description.test["testPattern"], test_pattern)
        else:
            scenario.set_global_headers(global_headers)
            test_description = self.get_test_description_v1(scenario)

        test_yaml = yaml.dump(test_description)
        # global_headers_json = json.dumps(global_headers)

        # combine all the scenarios into one test_description
        _call_function(
            _library.runTesterStartWrapper,
            [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_bool],
            ctypes.c_char_p,
            [
                namespace.encode(),
                address.encode(),
                test_yaml.encode(),
                True,
            ],
        )
        if blocked:
            tester_status_raw = _call_function(
                _library.runTesterStatusWrapper,
                [ctypes.c_char_p, ctypes.c_char_p],
                ctypes.c_char_p,
                [namespace.encode(), address.encode()],
                return_output=True,
            )

            tester_status = ""
            try:
                tester_status = json.loads(tester_status_raw)
            except ValueError as error:
                raise Exception(f"Could not parse tester status: {error}")

            if "status" not in tester_status:
                raise Exception(f"Could not parse tester status: {tester_status}")

            if tester_status["status"] == "finished":
                return

            if "error" in tester_status:
                raise Exception(f"Test failed: {tester_status['error']}")

            if "message" in tester_status:
                raise Exception(f"Test failed: {tester_status['message']}")

            raise Exception("Test failed")

    def set_global_rest_headers(self, global_headers) -> None:
        """
        Sets the global REST headers for this client.
        """
        self.global_headers=global_headers

    def get_test_description_v1(self, scenario: _Scenario) -> _TestDescription:
        """
        Helper for returning the test description for the scenario
        """
        steps = []
        request_dict = {}
        service_dict = {}
        endpoint_dict = {}

        for step_v1 in scenario.steps_v1:
            steps.append(step_v1.to_json())

            if isinstance(step_v1.step, _Request):
                request_dict[step_v1.step.name] = step_v1.step.as_request_dict(self.global_headers)

                for service in step_v1.step.endpoint_descriptor.services:
                    service_dict[service.get("name")] = service
                endpoint = step_v1.step.endpoint_descriptor.endpoint
                endpoint_dict[endpoint.get("name")] = endpoint

        # All of the endpoints and services are within the requests_v1 object
        return _TestDescription(
            version=SKYRAMP_YAML_VERSION,
            test={
                "testPattern": [{"startAt": scenario.start_at, "scenarioName": scenario.name}],
            },
            scenarios=[{"name": scenario.name, "steps": steps}],
            services=list(service_dict.values()),
            requests=list(request_dict.values()),
            endpoints=list(endpoint_dict.values()),
            )

def _new_client(kubeconfig_path: str) -> _Client:
    return _Client(
        kubeconfig_path=kubeconfig_path,
        context="kind-skyramp-local-kind-cluster",
        cluster_name="kind-cluster",
    )

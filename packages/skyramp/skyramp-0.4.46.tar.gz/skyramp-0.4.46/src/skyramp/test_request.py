"""
Contains helpers for interacting with Skyramp test request.
"""
from skyramp.endpoint import _Endpoint
from skyramp.rest_param import _RestParam as RestParam

class _Request:
    def __init__(self,
                 name: str,
                 endpoint_descriptor: _Endpoint,
                 method_type: str,
                 params: [RestParam]=None,
                 blob: str='',
                 headers: dict=None,
                 vars_: dict=None,
                 python: str='') -> None:
        self.name = name
        self.endpoint_descriptor = endpoint_descriptor
        self.method_type = method_type
        self.params = params
        self.blob = blob
        self.python = python
        self.headers = headers
        self.vars_ = vars_

    def _get_method_name_for_method_type(self):
        for method in self.endpoint_descriptor.endpoint.get("methods"):
            if method.get("type").lower() == self.method_type.lower():
                return method["name"]
        methods = self.endpoint_descriptor.endpoint.get('methods')
        raise Exception(f"method type {self.method_type} not found. Methods: {methods}")

    def to_json(self):
        """
        Convert the object to a JSON string.
        """
        return {
            "requestName": self.name
        }

    def as_request_dict(self, global_headers=None):
        """
        Convert the object to a JSON string.
        """

        endpoint_name = self.endpoint_descriptor.endpoint.get("name")
        if not endpoint_name:
            descriptor = self.endpoint_descriptor
            raise Exception(f"endpoint name not found. Endpoint descriptor: {descriptor}")

        request_dict = {
            "name": self.name,
            "endpointName": endpoint_name,
            "methodName": self._get_method_name_for_method_type(),
        }

        if global_headers or self.headers:
            request_dict["headers"] = {}
        if global_headers:
            request_dict["headers"] = global_headers
        if self.headers:
            request_dict["headers"] = request_dict["headers"] | self.headers
        if self.params:
            params = [param.to_json() for param in self.params]
            request_dict["params"] = params
        if self.blob:
            request_dict["blob"] = self.blob
        if self.python:
            request_dict["python"] = self.python
        if self.vars_:
            request_dict["vars"] = self.vars_

        return request_dict
    
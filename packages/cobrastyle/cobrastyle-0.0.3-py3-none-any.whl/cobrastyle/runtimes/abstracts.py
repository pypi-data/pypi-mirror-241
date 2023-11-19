from abc import ABC, abstractmethod
from http.client import HTTPResponse
from typing import Any

from cobrastyle.runtimes.models import Invocation


class AbstractLambdaClient(ABC):
    @abstractmethod
    def get_next_invocation(self) -> Invocation:
        pass

    @abstractmethod
    def post_invocation_response(self, aws_request_id: str, result: Any) -> HTTPResponse:
        pass

    @abstractmethod
    def post_invocation_error(self, aws_request_id: str) -> HTTPResponse:
        pass

    @abstractmethod
    def post_init_error(self) -> HTTPResponse:
        pass

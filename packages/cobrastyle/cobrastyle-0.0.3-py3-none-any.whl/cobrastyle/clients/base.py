from enum import Enum
from http.client import HTTPResponse
from typing import Optional
from urllib.parse import urljoin
from urllib.request import Request, urlopen

from cobrastyle.constants import AWS_LAMBDA_RUNTIME_API


class APIVersion(Enum):
    V_2018_06_01 = '2018-06-01'


class HTTPMethod(Enum):
    GET = 'GET'
    POST = 'POST'


class BaseLambdaClient:
    def __init__(
            self,
            api_host_port: Optional[str] = None,
            api_version: APIVersion = APIVersion.V_2018_06_01,
    ) -> None:
        api_host_port = api_host_port or AWS_LAMBDA_RUNTIME_API
        self.api_url = f'http://{api_host_port}/{api_version.value}/'

    def _request(
            self,
            path: str,
            *,
            method: HTTPMethod,
            data: Optional[bytes] = None,
    ) -> HTTPResponse:
        url = urljoin(self.api_url, path)
        request = Request(url, method=method.value, data=data)

        return urlopen(request)

    def _get(self, path: str) -> HTTPResponse:
        return self._request(path, method=HTTPMethod.GET)

    def _post(self, path: str, data: Optional[bytes] = None) -> HTTPResponse:
        return self._request(path, method=HTTPMethod.POST, data=data)

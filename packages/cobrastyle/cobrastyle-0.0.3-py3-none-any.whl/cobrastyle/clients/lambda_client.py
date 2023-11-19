import json
from http.client import HTTPResponse
from typing import Any

from cobrastyle.clients.base import BaseLambdaClient
from cobrastyle.runtimes.abstracts import AbstractLambdaClient
from cobrastyle.runtimes.models import ClientContext, CognitoIdentity, Invocation


class ClientContextJSONDecoder(json.JSONDecoder):
    def __init__(self):
        super().__init__(object_hook=self.decode_client_context)

    def decode_client_context(self, data: dict[str, Any]) -> ClientContext:
        return ClientContext(
            installation_id=data['installation_id'],
            app_title=data['app_title'],
            app_version_name=data['app_version_name'],
            app_version_code=data['app_version_code'],
            app_package_name=data['app_package_name'],
            custom=data['custom'],
            env=data['env'],
        )


class CognitoIdentityJSONDecoder(json.JSONDecoder):
    def __init__(self):
        super().__init__(object_hook=self.decode_cognito_identity)

    def decode_cognito_identity(self, data: dict[str, Any]) -> CognitoIdentity:
        return CognitoIdentity(
            cognito_identity_id=data['cognito_identity_id'],
            cognito_identity_pool_id=data['cognito_identity_pool_id'],
        )


def get_invocation(response: HTTPResponse) -> Invocation:
    event = json.loads(response.read().decode('utf-8'))
    aws_request_id = response.headers['Lambda-Runtime-Aws-Request-Id']
    runtime_deadline = response.headers['Lambda-Runtime-Deadline-Ms']
    invoked_function_arn = response.headers['Lambda-Runtime-Invoked-Function-Arn']
    trace_id = response.headers.get('Lambda-Runtime-Trace-Id')

    if context_value := response.headers.get('Lambda-Runtime-Client-Context'):
        client_context = json.loads(context_value, object_hook=ClientContextJSONDecoder)
    else:
        client_context = None

    if identity_value := response.headers.get('Lambda-Runtime-Cognito-Identity'):
        cognito_identity = json.loads(identity_value, object_hook=CognitoIdentityJSONDecoder)
    else:
        cognito_identity = None

    return Invocation(
        event=event,
        aws_request_id=aws_request_id,
        runtime_deadline=runtime_deadline,
        invoked_function_arn=invoked_function_arn,
        trace_id=trace_id,
        client_context=client_context,
        cognito_identity=cognito_identity,
    )


class LambdaClient(AbstractLambdaClient, BaseLambdaClient):
    """https://docs.aws.amazon.com/lambda/latest/dg/runtimes-api.html"""

    def get_next_invocation(self) -> Invocation:
        path = 'runtime/invocation/next'

        with self._get(path) as response:
            return get_invocation(response)

    def post_invocation_response(self, aws_request_id: str, result: Any) -> HTTPResponse:
        path = f'runtime/invocation/{aws_request_id}/response'
        data = json.dumps(result).encode('utf-8')

        return self._post(path, data)

    def post_invocation_error(self, aws_request_id: str) -> HTTPResponse:
        path = f'runtime/invocation/{aws_request_id}/error'
        data = 'INVOCATION ERROR'.encode('utf-8')

        return self._post(path, data)

    def post_init_error(self) -> HTTPResponse:
        path = '/runtime/init/error'
        data = 'INIT ERROR'.encode('utf-8')

        return self._post(path, data)

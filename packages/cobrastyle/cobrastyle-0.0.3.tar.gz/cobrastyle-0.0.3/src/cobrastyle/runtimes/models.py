import time
from dataclasses import dataclass
from typing import Any


@dataclass
class ClientContext:
    installation_id: str
    app_title: str
    app_version_name: str
    app_version_code: str
    app_package_name: str
    custom: dict
    env: dict


@dataclass
class CognitoIdentity:
    cognito_identity_id: str
    cognito_identity_pool_id: str


@dataclass
class Invocation:
    event: dict[str, Any]
    aws_request_id: str
    runtime_deadline: int
    invoked_function_arn: str
    client_context: ClientContext | None
    cognito_identity: CognitoIdentity | None
    trace_id: str | None = None


@dataclass
class Context:
    """https://docs.aws.amazon.com/lambda/latest/dg/python-context.html"""

    function_name: str
    function_version: str
    invoked_function_arn: str
    memory_limit_in_mb: int
    runtime_deadline: int
    aws_request_id: str
    log_group_name: str
    log_stream_name: str
    client_context: ClientContext | None
    identity: CognitoIdentity | None

    def get_remaining_time(self) -> int:
        """Return the remaining time (in milliseconds) before Lambda times out."""

        return int(self.runtime_deadline - time.time() * 1000)

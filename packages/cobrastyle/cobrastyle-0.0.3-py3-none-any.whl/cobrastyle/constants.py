import os

# Reserved environment variables
_HANDLER = os.getenv('_HANDLER')  # TODO: not used, remove?
_X_AMZN_TRACE_ID = os.getenv('_X_AMZN_TRACE_ID')  # TODO: not used, remove?

AWS_DEFAULT_REGION = os.getenv('AWS_DEFAULT_REGION')  # TODO: not used, remove?
AWS_REGION = os.getenv('AWS_REGION')  # TODO: not used, remove?
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')  # TODO: not used, remove?
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')  # TODO: not used, remove?
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')  # TODO: not used, remove?
AWS_SESSION_TOKEN = os.getenv('AWS_SESSION_TOKEN')  # TODO: not used, remove?

AWS_EXECUTION_ENV = os.getenv('AWS_EXECUTION_ENV')  # TODO: not used, remove?
AWS_LAMBDA_FUNCTION_NAME = os.getenv('AWS_LAMBDA_FUNCTION_NAME')
AWS_LAMBDA_FUNCTION_VERSION = os.getenv('AWS_LAMBDA_FUNCTION_VERSION')
AWS_LAMBDA_FUNCTION_MEMORY_SIZE = os.getenv('AWS_LAMBDA_FUNCTION_MEMORY_SIZE')
AWS_LAMBDA_INITIALIZATION_TYPE = os.getenv('AWS_LAMBDA_INITIALIZATION_TYPE')  # TODO: not used, remove?
AWS_LAMBDA_RUNTIME_API = os.getenv('AWS_LAMBDA_RUNTIME_API')

AWS_LAMBDA_LOG_GROUP_NAME = os.getenv('AWS_LAMBDA_LOG_GROUP_NAME')
AWS_LAMBDA_LOG_STREAM_NAME = os.getenv('AWS_LAMBDA_LOG_STREAM_NAME')

LAMBDA_TASK_ROOT = os.getenv('LAMBDA_TASK_ROOT')  # TODO: not used, remove?
LAMBDA_RUNTIME_DIR = os.getenv('LAMBDA_RUNTIME_DIR')  # TODO: not used, remove?

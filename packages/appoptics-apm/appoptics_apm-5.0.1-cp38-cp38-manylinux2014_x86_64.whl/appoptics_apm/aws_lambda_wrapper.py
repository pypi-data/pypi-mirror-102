#    Copyright 2021 SolarWinds, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
""" AppOptics APM instrumentation for serverless AWS Lambda applications.
"""
import importlib
import logging
import os

import appoptics_apm

logger = logging.getLogger(__name__)


def wrap_lambda_handler():
    """Wraps the original AWS lambda function.
    The name of the lambda function is expected to be provided in an environment variable called
    'APPOPTICS_WRAP_LAMBDA_HANDLER'. The variable is expected to specify a lambda function handler in the form
    'module.function_handler'. If this variable is not set, or if the value of the variable does not specify a Python
    callable, the agent will raise an Exception.
    """
    if not appoptics_apm.SwigContext.isLambda():
        return None
    error_msg_help = 'Please specify your original Lambda function in the form `module.function_handler`.'
    envv_name = 'APPOPTICS_WRAP_LAMBDA_HANDLER'
    envv_val = os.environ.get(envv_name, '')
    if envv_val == '':
        raise Exception('{} environment variable is not set. '.format(envv_name) + error_msg_help)

    target = envv_val.rsplit('.', 1)
    if len(target) < 2:
        raise Exception('Invalid {}: {}. '.format(envv_name, envv_val) + error_msg_help)

    try:
        target_module = importlib.import_module(target[0])
        target_handler = getattr(target_module, target[1])
    except (ModuleNotFoundError, AttributeError) as e:
        # ModuleNotFoundError is not available in Python2.7, but we do not support 2.7 under a AWS Lambda environment
        raise Exception('Invalid {}: {}, {}. '.format(envv_name, envv_val, e) + error_msg_help)

    if not callable(target_handler):
        raise Exception(
            'Invalid function handler provided {}: {}. The handler {} is not callable. '.format(
                envv_name, envv_val, target_handler) + error_msg_help)

    return target_handler


target_handler = wrap_lambda_handler()

# track invocation count
invocation_count = 0


def handler(event, context):
    """This function is the wrapping function which instruments the original Lambda function specified in the
    target_handler"""
    global invocation_count
    invocation_count += 1

    incoming_xtr = None
    layer = 'aws_lambda_python'
    appoptics_apm.start_trace(
        layer,
        xtr=incoming_xtr,
        keys={
            'Spec': 'aws-lambda',
            'FunctionVersion': context.function_version,
            'InvokedFunctionARN': context.invoked_function_arn,
            'AWSRequestID': context.aws_request_id,
            'AWSRegion': os.environ.get('AWS_REGION'),
            'InvocationCount': invocation_count,
            'MemoryLimitInMB': context.memory_limit_in_mb,
            'LogStreamName': context.log_stream_name,
        })
    appoptics_apm.set_transaction_name(context.function_name)

    result = None
    try:
        result = target_handler(event, context)
    except Exception:
        appoptics_apm.log_exception()
        raise
    finally:
        appoptics_apm.end_trace(layer)

    return result

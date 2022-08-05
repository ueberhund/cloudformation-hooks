from email.message import Message
import logging
from typing import Any, MutableMapping, Optional

from cloudformation_cli_python_lib import (
    BaseHookHandlerRequest,
    HandlerErrorCode,
    Hook,
    HookInvocationPoint,
    OperationStatus,
    ProgressEvent,
    SessionProxy,
    exceptions,
)

from .models import HookHandlerRequest, TypeConfigurationModel

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)
TYPE_NAME = "AWSNonprofits::gmike::Tagging"

LOG.setLevel(logging.INFO)

hook = Hook(TYPE_NAME, TypeConfigurationModel)
test_entrypoint = hook.test_entrypoint


@hook.handler(HookInvocationPoint.CREATE_PRE_PROVISION)
def pre_create_handler(
        session: Optional[SessionProxy],
        request: HookHandlerRequest,
        callback_context: MutableMapping[str, Any],
        type_configuration: TypeConfigurationModel
) -> ProgressEvent:
    target_model = request.hookContext.targetModel
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS
    )
    
    error_code = None 
    message = None
    
    target_name = request.hookContext.targetName
    status=OperationStatus.SUCCESS,
    message="Successfully invoked PreUpdateHookHandler for target: " + target_name
    resource_properties = request.hookContext.targetModel.get("resourceProperties")
    
    try:
        if "AWS::S3::Bucket" == target_name: 
             #Look at the tags on the bucket
            resource_tags = resource_properties.get("Tags")
            status = None 
            
            if not resource_tags:
                status = OperationStatus.FAILED
                message = f"Resource does not have tags"
            else:
                found_tag = False
                for tag in resource_tags:
                    if tag['Key'] == 'organization-id':
                        found_tag = True
                        status = OperationStatus.SUCCESS    
                        break
                if not found_tag:
                    status = OperationStatus.FAILED
                    message = f"Resource does not have the correct organization-id tag"
                
            if status == OperationStatus.FAILED:
                error_code = HandlerErrorCode.NonCompliant

    except TypeError as e:
        raise exceptions.InternalFailure(f"was not expecting type {e}")
        
    return ProgressEvent(
            status=status,
            message=message,
            errorCode=error_code
        )


@hook.handler(HookInvocationPoint.UPDATE_PRE_PROVISION)
def pre_update_handler(
        session: Optional[SessionProxy],
        request: BaseHookHandlerRequest,
        callback_context: MutableMapping[str, Any],
        type_configuration: TypeConfigurationModel
) -> ProgressEvent:
    target_model = request.hookContext.targetModel
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS
    )
    
    error_code = None 
    message = None
    
    target_name = request.hookContext.targetName
    status=OperationStatus.SUCCESS,
    message="Successfully invoked PreUpdateHookHandler for target: " + target_name
    resource_properties = request.hookContext.targetModel.get("resourceProperties")
    
    try: 
        if "AWS::S3::Bucket" == target_name: 
            #Look at the tags on the bucket
            resource_tags = resource_properties.get("Tags")
            status = None 
            
            if not resource_tags:
                status = OperationStatus.FAILED
                message = f"Resource does not have tags"
            else:
                found_tag = False
                for tag in resource_tags:
                    if tag['Key'] == 'organization-id':
                        found_tag = True
                        status = OperationStatus.SUCCESS    
                        break
                if not found_tag:
                    status = OperationStatus.FAILED
                    message = f"Resource does not have the correct organization-id tag"
                
            if status == OperationStatus.FAILED:
                error_code = HandlerErrorCode.NonCompliant

    except TypeError as e:
        raise exceptions.InternalFailure(f"was not expecting type {e}")
        
    return ProgressEvent(
            status=status,
            message=message,
            errorCode=error_code
        )


@hook.handler(HookInvocationPoint.DELETE_PRE_PROVISION)
def pre_delete_handler(
        session: Optional[SessionProxy],
        request: BaseHookHandlerRequest,
        callback_context: MutableMapping[str, Any],
        type_configuration: TypeConfigurationModel
) -> ProgressEvent:
    # TODO: put code here
    return ProgressEvent(
        status=OperationStatus.SUCCESS
    )

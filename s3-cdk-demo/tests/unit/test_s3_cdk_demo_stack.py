import aws_cdk as core
import aws_cdk.assertions as assertions

from s3_cdk_demo.s3_cdk_demo_stack import S3CdkDemoStack

# example tests. To run these tests, uncomment this file along with the example
# resource in s3_cdk_demo/s3_cdk_demo_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = S3CdkDemoStack(app, "s3-cdk-demo")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

from aws_cdk import (
    # Duration,
    Stack,
    Tags,
    aws_s3 as s3
)
from constructs import Construct

class S3CdkDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a bucket 
        s3_bucket = s3.Bucket(self, id='bucket-example')
        Tags.of(s3_bucket).add("organization-id","sampe-value") 

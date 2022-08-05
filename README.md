# cloudformation-hooks
This repo is a demo showing how to build and use CloudFormation hooks. [Read here](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks.html) for more information on CloudFormation hooks.

[This AWS workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/f09fd78b-ef8a-4a9d-9d2b-f31a3e6ca956/en-US/python/initiating) also provides a good walkthrough on creating, testing, and deploying a CloudFormation hook.

The [cfn-hook-demo](./cfn-hook-demo) folder contains the code for a hook at requires an "organization-id" tag be applied to an S3 bucket before it will allow it to be created. The code for the hook is in the [myhook](./cfn-hook-demo/myhook) folder. Make sure you know how to [register a hook](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/registering-hook-python.html). The `bad-bucket.yaml` and `good-bucket.yaml` files in the root directory are sample templates you can use to test the code out. The `bad-bucket.yaml` file should result in a stack error when the hook is running. Likewise the `good-bucket.yaml` file should create a bucket successfully.

The [s3-cdk-demo](./s3-cdk-demo) folder contains the code for creating a bucket via the CDK. If you `cdk synth` and `cdk deploy`, the code should work as-is. However, if you want to test a negative case, comment out line 16 of [s3_cdk_demo_stack.py](./s3-cdk-demo/s3_cdk_demo/s3_cdk_demo_stack.py), which will turn off tagging on the bucket.

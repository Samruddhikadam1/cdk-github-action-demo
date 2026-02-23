from aws_cdk import NestedStack
from constructs import Construct
from constructs.s3_construct import S3Construct

class S3NestedStack(NestedStack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        S3Construct(
            self,
            "MyBucket",
            bucket_name="isa-demo-bucket-infra"
        )
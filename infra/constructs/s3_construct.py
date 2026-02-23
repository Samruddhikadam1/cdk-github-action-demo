from aws_cdk import (
    aws_s3 as s3,
    RemovalPolicy
)
from constructs import Construct

class S3Construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, bucket_name: str):
        super().__init__(scope, construct_id)

        self.bucket = s3.Bucket(
            self,
            "S3Bucket",
            bucket_name=bucket_name,
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True
        )
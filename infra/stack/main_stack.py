from aws_cdk import Stack
from constructs import Construct
from domain.lambda_stack import LambdaNestedStack
from domain.s3_stack import S3NestedStack

class MainStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        LambdaNestedStack(self, "LambdaNested")
        S3NestedStack(self, "S3Nested")
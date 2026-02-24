from aws_cdk import NestedStack
from constructs import Construct
from constructs.lambda_construct import LambdaConstruct

class LambdaNestedStack(NestedStack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        LambdaConstruct(
            self,
            "MyLambda",
            function_name="my-python-lambda"
        )

        LambdaConstruct(
            self,
            "MyLambda1",
            function_name="my-python-lambda1"
        )
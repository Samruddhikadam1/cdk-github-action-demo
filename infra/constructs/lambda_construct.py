from aws_cdk import (
    aws_lambda as _lambda,
)
from constructs import Construct

class LambdaConstruct(Construct):

    def __init__(self, scope: Construct, construct_id: str, function_name: str):
        super().__init__(scope, construct_id)

        self.lambda_function = _lambda.Function(
            self,
            "LambdaFunction",
            function_name=function_name,
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="handler.handler",  # file.function
            code=_lambda.Code.from_asset("lambda"),  # points to infra/lambda
        )
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_iam as iam
)
from constructs import Construct

class LambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        lambda_role = iam.Role(
            self,
            "LambdaExecutionRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "service-role/AWSLambdaBasicExecutionRole"
                )
            ]
        )

        _lambda.Function(
            self,
            "HelloLambda",
            runtime=_lambda.Runtime.PYTHON_3_10,
            handler="handler.handler",
            code=_lambda.Code.from_asset("lambda"),
            role=lambda_role
        )

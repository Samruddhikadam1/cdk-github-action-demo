import aws_cdk as cdk
from stacks.lambda_stack import LambdaStack

app = cdk.App()

LambdaStack(app, "LambdaStack")

app.synth()

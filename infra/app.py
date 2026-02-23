#!/usr/bin/env python3
import aws_cdk as cdk
from stack.main_stack import MainStack

app = cdk.App()

MainStack(
    app,
    "MyInfraStack",
    env=cdk.Environment(
        account=app.node.try_get_context("account"),
        region=app.node.try_get_context("region")
    )
)

app.synth()
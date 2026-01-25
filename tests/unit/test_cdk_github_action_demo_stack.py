import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_github_action_demo.cdk_github_action_demo_stack import CdkGithubActionDemoStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_github_action_demo/cdk_github_action_demo_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkGithubActionDemoStack(app, "cdk-github-action-demo")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

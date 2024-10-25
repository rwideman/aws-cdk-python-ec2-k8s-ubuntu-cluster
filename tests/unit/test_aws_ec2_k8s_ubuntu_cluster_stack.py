import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_ec2_k8s_ubuntu_cluster.aws_ec2_k8s_ubuntu_cluster_stack import AwsEc2K8SUbuntuClusterStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_ec2_k8s_ubuntu_cluster/aws_ec2_k8s_ubuntu_cluster_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsEc2K8SUbuntuClusterStack(app, "aws-ec2-k8s-ubuntu-cluster")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

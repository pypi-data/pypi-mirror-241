from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
)
from constructs import Construct

class AsaasSqsModuleStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, name: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(
            self, "AsaasSqsModuleQueue",
            queue_name=name,
            visibility_timeout=Duration.seconds(300),
        )

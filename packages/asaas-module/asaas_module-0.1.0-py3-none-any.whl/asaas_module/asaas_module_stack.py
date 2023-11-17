from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
)
from constructs import Construct

class AsaasModuleStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, queue_name: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(self, 
            construct_id, 
            queue_name=queue_name,
            visibility_timeout=Duration.seconds(300),
            )

from aws_cdk import Stack
from aws_cdk import aws_events as events
from aws_cdk import aws_lambda as lambda_
from aws_cdk import aws_events_targets as targets
from aws_cdk import aws_iam as iam
from constructs import Construct


class LambdaBatchStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, config, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ########################################################
        # Lambdaの定義
        ########################################################

        # Create the Lambda function
        lambda_fn = lambda_.Function(
            self,
            'Lambda',
            runtime=lambda_.Runtime.PYTHON_3_8,
            handler='index.handler',    
            code=lambda_.Code.from_asset('lambda'),
        )

        # Grant CloudWatch Logs permissions to the Lambda function
        lambda_fn.add_to_role_policy(
            iam.PolicyStatement(
                actions=['logs:CreateLogGroup', 'logs:CreateLogStream', 'logs:PutLogEvents'],
                resources=['*'],
            )
        )
        
        ########################################################
        # EventBridgeの定義
        ########################################################

        # Create the EventBridge rule
        rule = events.Rule(
            self,
            'Rule',
            schedule=events.Schedule.cron(
                minute=config['event']['schedule']['minute'],
                hour=config['event']['schedule']['hour'],
                month=config['event']['schedule']['month'],
                week_day=config['event']['schedule']['week_day'],
                year=config['event']['schedule']['year'],
            ),
        )

        # Add the Lambda function as the target for the EventBridge rule
        rule.add_target(targets.LambdaFunction(lambda_fn))
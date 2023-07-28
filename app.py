#!/usr/bin/env python3
import aws_cdk as cdk
import yaml

from stacks.lambda_batch_stack import LambdaBatchStack

with open('configs/config.yaml', 'r') as yml:
    config = yaml.safe_load(yml)

app = cdk.App()

lambda_batch_stack = LambdaBatchStack(
    app,
    "LambdaBatchStack",
    config=config,
    env=cdk.Environment(account=config['account']['account_id'], region=config['account']['region']),
    )

app.synth()

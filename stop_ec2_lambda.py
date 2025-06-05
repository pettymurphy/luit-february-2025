# stop_ec2_lambda.py

import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Describe running instances
    response = ec2.describe_instances(Filters=[
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ])

    # Extract instance IDs
    instance_ids = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])

    # Stop instances if any are found
    if instance_ids:
        ec2.stop_instances(InstanceIds=instance_ids)
        return {
            'statusCode': 200,
            'body': f'Stopped instances: {instance_ids}'
        }
    else:
        return {
            'statusCode': 200,
            'body': 'No running instances found.'
        }

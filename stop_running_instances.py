import boto3

def lambda_handler(event=None, context=None):
    ec2 = boto3.client('ec2', region_name='us-east-1')

    # Describe all instances
    response = ec2.describe_instances(
        Filters=[
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
    )

    # Extract Instance IDs of running instances
    instance_ids = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])

    # Stop the instances if there are any
    if instance_ids:
        stopping = ec2.stop_instances(InstanceIds=instance_ids)
        print(f"Stopping instances: {instance_ids}")
        return stopping
    else:
        print("No running instances found.")
        return "No instances to stop."

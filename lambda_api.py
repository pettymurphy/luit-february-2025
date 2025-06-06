import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    key = event.get('queryStringParameters', {}).get('key')
    value = event.get('queryStringParameters', {}).get('value')

    if not key or not value:
        return {
            'statusCode': 400,
            'body': 'Missing query parameters: key and value are required.'
        }

    filters = [
        {
            'Name': f'tag:{key}',
            'Values': [value]
        },
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]

    response = ec2.describe_instances(Filters=filters)

    instance_ids = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])

    if instance_ids:
        ec2.stop_instances(InstanceIds=instance_ids)
        return {
            'statusCode': 200,
            'body': f'Stopped instances: {instance_ids}'
        }
    else:
        return {
            'statusCode': 200,
            'body': 'No running instances found with the given tag.'
        }

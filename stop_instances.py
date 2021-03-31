import json
import boto3
region = 'us-east-1'
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    filters = [
                { 'Name': 'instance-state-name',
                  'Values': ['running'],
                }
            ]

    response = ec2.describe_instances(Filters=filters)

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instanceId = instance["InstanceId"]
            print("Stopping instanceID = %s" % instanceId)
            ec2.stop_instances(InstanceIds=[instanceId],DryRun=True)

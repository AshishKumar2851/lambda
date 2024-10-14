import boto3

#def lambda_handler(event, context):
client = boto3.client('ec2')
response = client.run_instances(

    ImageId = 'ami-078264b8ba71bc45e',
    InstanceType = 't2.micro',
    KeyName = 'Ashish_DevOps_pem',
    MaxCount = 1,
    MinCount = 1,
)


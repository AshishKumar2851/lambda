import boto3

client = boto3.client('ec2')

response = client.terminate_instances(
    InstanceIds=[
        'i-03578e81f1318f568','i-0839c6137cef4bff5',
    ],
#    Hibernate=True|False,
#    DryRun=True
    Force=True
)
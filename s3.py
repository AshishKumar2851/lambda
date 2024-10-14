import boto3

client = boto3.client('s3')
response = client.create_bucket(
    Bucket='parvboto3bucket',

    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1',
    }
)
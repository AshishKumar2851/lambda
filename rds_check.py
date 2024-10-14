import boto3
import time

rds_client = boto3.client('rds', region_name='ap-south-1')
# Check RDS instance status
while True:
    try:
        response = rds_client.describe_db_instances(DBInstanceIdentifier='my-db-instance')
        db_instance_status = response['DBInstances'][0]['DBInstanceStatus']
        print(f"Current status of DB instance {'my-db-instance'}: {db_instance_status}")

        if db_instance_status == 'available':
            print("RDS instance is available.")
            break

        time.sleep(30)  # Wait for 30 seconds before checking again
    except Exception as e:
        print(f"Error checking DB instance status: {e}")
        break

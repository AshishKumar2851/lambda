import boto3

# Initialize a session using Boto3
rds_client = boto3.client('rds', region_name='ap-south-1')

# Define the RDS instance parameters
db_instance_identifier = 'my-db-instance'
db_instance_class = 'db.t3.micro'  # Example: Use an instance type like db.t3.micro
engine = 'mysql'
master_username = 'admin'
master_user_password = 'Cloud123'
db_name = 'testdb'

# Create the RDS instance
try:
    response = rds_client.create_db_instance(
        DBInstanceIdentifier=db_instance_identifier,
        AllocatedStorage=20,  # Storage size in GB
        DBInstanceClass=db_instance_class,
        Engine=engine,
        MasterUsername=master_username,
        MasterUserPassword=master_user_password,
        DBName=db_name,
    #    BackupRetentionPeriod=7,  # Retain backups for 7 days
    #    MultiAZ=False,
    #    PubliclyAccessible=True,  # Set to True if you want the DB to be accessible from the internet
    #    VpcSecurityGroupIds=['sg-xxxxxxxx'],  # Replace with your security group ID
    )
    print("RDS instance is being created.")
except Exception as e:
    print(f"Error creating RDS instance: {e}")

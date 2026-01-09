import os
import boto3
from botocore.config import Config

def run():
    # These names must match your YAML env keys exactly
    bucket = os.environ.get('INPUT_BUCKET')
    dist_folder = os.environ.get('INPUT_DIST-FOLDER')
    region = os.environ.get('INPUT_BUCKET-REGION', 'us-east-1')
    
    # Access Keys passed from the 'env:' block in your workflow
    aws_id = os.environ.get('AWS_ACCESS_KEY_ID')
    aws_key = os.environ.get('AWS_SECRET_ACCESS_KEY')

    s3_client = boto3.client(
        's3',
        region_name=region,
        aws_access_key_id=aws_id,
        aws_secret_access_key=aws_key
    )

    # ... rest of your upload logic ...
    print(f"Deploying to {bucket}...")

if __name__ == "__main__":
    run()
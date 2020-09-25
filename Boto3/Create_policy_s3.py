#!/usr/bin/env python3
import boto3
import json

#Setting a bucket policy
bucket_name = 'dgruploads-bucket'
bucket_policy = {
        'Version': '2012-10-17',
        'Statement': [{
                'Sid': 'AddPerm',
                'Effect': 'Allow',
                'Principal': '*',
                'Action': ['s3:GetObject'],
                'Resource': f'arn:aws:s3:::{bucket_name}/*'
        }]
}

#Convert the policy from json dict to string
bucket_policy = json.dumps(bucket_policy)

#Set the new bucket policy
s3 = boto3.client('s3')
s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)

#Retrieve the policy of the specified bucket
s3 = boto3.client('s3')
result = s3.get_bucket_policy(Bucket='dgruploads-bucket')
print (result['Policy'])

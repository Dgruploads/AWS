#!/usr/bin/python3

import boto3

client = boto3.client('iam')

response = client.create_user(
  UserName = "test_user",
  Tags = [
     {
       'Key':'Name',
       'Value':'test_user'
     },
  ]
)

print (response)

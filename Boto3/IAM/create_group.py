#!/usr/bin/python3

import boto3

client = boto3.client('iam')


group_name = input("Enter the group name : ")
user_name = input("Enter the user name : ")

response = client.create_group(
  GroupName = group_name
)

response = client.add_user_to_group(
  UserName = user_name,
  GroupName = group_name
)

print (response)

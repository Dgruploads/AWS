#!/usr/bin/python3

import boto3

client = boto3.client('iam')

group_name = input("Enter the group name : ")

response = client.attach_group_policy(
  GroupName = group_name,
  PolicyArn = "arn:aws:iam::aws:policy/AdministratorAccess"
)

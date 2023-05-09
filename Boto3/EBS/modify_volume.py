#!/usr/bin/python3

import boto3
client = boto3.client('ec2',region_name="us-east-1")

volume_id = input("Enter the volume Id to modify :")

response = client.modify_volume(
  VolumeId=volume_id,
  Size=20,
  VolumeType="gp2",
)

print(response)

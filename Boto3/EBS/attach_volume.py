#!/usr/bin/python3

import boto3

client = boto3.client('ec2',region_name="us-east-1")

device_name = input("Enter the devie name : ")
instance_id = input("Enter the instance ID : ")
volume_id = input("Enter the volume ID : ")

response = client.attach_volume(
  Device=device_name,
  InstanceId=instance_id,
  VolumeId=volume_id
)

print(response)

#!/usr/bin/python3
import boto3

client = boto3.client('ec2',region_name="us-east-1")
response = client.create_volume(
  AvailabilityZone="us-east-1a",
  Size=10,
  VolumeType="gp2",
  TagSpecifications=[
    {
     'ResourceType': 'volume',
     'Tags': [
       {
        'Key':'Name',
        'Value':'Python'
       },
     ]
    },
  ]
)

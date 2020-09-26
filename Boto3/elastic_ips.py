#!/usr/bin/env python3
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

#Describe elastic ip address
filters = [
	{'Name' : 'domain', 'Values' : ['vpc']}
]
response = ec2.describe_addresses(Filters = filters)
print (response)

#Allocate and associate an EIP with an instance
try:
	allocation = ec2.allocate_address(Domain='vpc-00f6f586c20bfc847')
	response = ec2.associate_address(AllocationId = allocation['AllocationId'],
					 InstanceId = 'i-0bb78de9c0fafa1bc')
	print (response)
except ClientError as e:
	print (e)

#Describe elastic ip address
filters = [
	{'Name' : 'domain', 'Values' : ['vpc']}
]
response = ec2.describe_addresses(Filters = filters)
print (response)

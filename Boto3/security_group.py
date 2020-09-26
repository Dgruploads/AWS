#!/usr/bin/env python3
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

#Showing the existing securitu group
try:
	response = ec2.describe_security_groups(GroupIds = ['sg-02c1e6c8bd137c4b5'])
	print (response)
except ClientError as e:
	print (e)

#Creating a new security group
response = ec2.describe_vpcs()
vpc_id = response.get('VPCs',[{}])[0].get('VPCid','')

try:
	response = ec2.create_security_group(GroupName = "Boto_security_group",
										 Description = "Boto_security_group",
										 VpcId = vpc_id)
	security_group_id = response['GroupId']
	print ("Security group created %s in vpc %s." %(security_group_id,vpc_id))

	data = ec2.authorize_security_group_ingress(
		GroupId = security_group_id,
		IpPermissions = [
			{'IpProtocol' : 'tcp',
			 'FromPort' : 22,
			 'ToPort' : 22,
			 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
			{'IpProtocol' : 'tcp',
			 'FromPort' : 80,
			 'ToPort' : 80,
			 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
			{'IpProtocol' : 'tcp',
			 'FromPort' : 443,
			 'ToPort' : 443,
			 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
			 ])	
	print ("Ingress successfully set %s" %data)
except ClientError as e :
	print (e)

#Showing the existing securitu group
try:
	response = ec2.describe_security_groups(GroupIds = ['sg-02c1e6c8bd137c4b5'])
	print (response)
except ClientError as e:
	print (e)

#!/usr/bin/env python3
import boto3

#Describe the EC2 instances
print ("Showing the existing instance")
ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print (response)

#Launch a new EC2 instance
launch = ec2.run_instances(
        InstanceType = "t2.micro",
        MaxCount = 1,
        MinCount = 1,
        ImageId = "ami-0947d2ba12ee1ff75"
        )
print (launch)

#Describe the EC2 instances
print()
print()
print("Showing new instances with existing instances")
ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print (response)

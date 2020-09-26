#!/usr/bin/env python3
import boto3

#Describe the existing key pairs
print ("Showing the existing key pairs")
ec2 = boto3.client('ec2')
response = ec2.describe_key_pairs()
print (response)

#Creating new key pairs
ec2 = boto3.client('ec2')
response = ec2.create_key_pair(KeyName = 'boto-key-pair')

#Describe the existing key pairs
print ("Showing the existing key pairs")
ec2 = boto3.client('ec2')
response = ec2.describe_key_pairs()
print (response)

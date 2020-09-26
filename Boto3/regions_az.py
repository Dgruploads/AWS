#!/usr/bin/env python3
import boto3

ec2 = boto3.client('ec2')

#Showing all the regions of EC2
response = ec2.describe_regions()
print ('Regions :', response['Regions'])

#Showing all the availability zones of EC2
response = ec2.describe_availability_zones()
print ('Avalability_zones :',response['AvailabilityZones'])

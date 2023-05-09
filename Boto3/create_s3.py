#!/usr/bin/env python3
import boto3

#Using S3 service
s3 = boto3.resource('s3')

#Print the list of available buckets
print ("Existing buckets :")
for bucket in s3.buckets.all():
	print (bucket.name)

#Create a new bucket
s3.create_bucket(Bucket='dgruploads-bucket')

#Print the list of available bucket
print ("Existing buckets :")
for bucket in s3.buckets.all():
	print (bucket.name)

#Upload a new file
data = open("index.html","rb")
s3.Bucket("dgruploads-bucket").put_object(Key="index.html", Body=data)

# Delete the S3 bucket
delete_bucket = client.delete_bucket(
    Bucket='dgruploads-bucket',
)
print(delete_bucket)

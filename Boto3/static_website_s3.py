#!/usr/bin/env python3
import boto3

#Define the website configuration
website_configuration = {
        'ErrorDocument' : {'Key' : 'error.html'},
        'IndexDocument' : {'Suffix' : 'index.html'},
        }

#Set the website configuration
s3 = boto3.client('s3')
s3.put_bucket_website(Bucket='dgruploads-bucket',WebsiteConfiguration=website_configuration)

#Retrieve the website configuration
result = s3.get_bucket_website(Bucket='dgruploads-bucket')
print (result)

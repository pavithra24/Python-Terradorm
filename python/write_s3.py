from datetime import datetime
from secrets import access_key, secret_access_key

import boto3
import boto3.session
import os
import sys

#main function
def main():
    #Creating Session With Boto3.
    session = boto3.Session(
    aws_access_key_id= access_key,
    aws_secret_access_key= secret_access_key
    )

    #Create file name with date and time as prefix
    date_string = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
    file_name = date_string + "_ file.txt"

    #Choose bucket name based on env pass the env through CLI
    env=(sys.argv[1]).upper();
    if env == 'QA':
        upload_file_bucket = 'qa-firstname-lastname-platform-challenge-67896'
    elif env == 'STAGE':
        upload_file_bucket = 'staging-firstname-lastname-platform-challenge-67896'
    else:
        print('Invalid stage?')
        return

    #Creating S3 Resource From the Session.
    s3 = session.resource('s3')

    object = s3.Object(upload_file_bucket, file_name)

    txt_data = b'This is the content of the file upload'

    result = object.put(Body=txt_data)

    res = result.get('ResponseMetadata')

    if res.get('HTTPStatusCode') == 200:
        print('File Uploaded Successfully')
    else:
        print('File Not Uploaded')


if __name__== "__main__":
    main()


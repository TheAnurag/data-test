import boto3

AWS_BUCKET_NAME = 'aj-data-test'

s3 = boto3.client('s3', 
            aws_access_key_id='AKIAJCXTW37QIFRHKRPA',
            aws_secret_access_key='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')

s3_object_name = 'test-data.json'
s3.upload_file(s3_object_name, AWS_BUCKET_NAME, s3_object_name)

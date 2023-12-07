import boto3
from urllib.parse import unquote_plus

# initialize s3 client
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # get source bucket and key from event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_key = unquote_plus(event['Records'][0]['s3']['object']['key'])

    # set target bucket
    target_bucket = 'yhb-wordfreq-processing'

    # try to copy object
    try:
        # set parameters for copy operation
        copy_source = {
            'Bucket': source_bucket,
            'Key': source_key
        }
        # using .copy() method to copy object
        s3_client.copy(copy_source, target_bucket, source_key)
        # return success response
        return {
            'statusCode': 200,
            'body': f"Successfully copied {source_key} from {source_bucket} to {target_bucket}"
        }
    except Exception as e:
        print(e)
        # return error response
        return {
            'statusCode': 500,
            'body': f"Error copying {source_key}: {str(e)}"
        }


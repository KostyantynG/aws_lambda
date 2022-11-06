import boto3

def count_words():
    s3 = boto3.client('s3')
    bucket='challenge-bucket-lambda'
    result = s3.list_objects(Bucket = bucket)
    for obj in result.get('Contents'):
        key = (obj['Key'])
    data = s3.get_object(Bucket=bucket, Key=key)
    file_contents = data['Body'].read()
    extracted_data = file_contents.decode("utf-8")
    words = extracted_data.split()
    final_data = f"The word count in the file {key} is {len(words)}"
    return final_data


def lambda_handler(event, context):
    client = boto3.client('sns')
    snsArn = 'arn:aws:sns:us-west-2:354207115246:word-count-topic'
    msg = count_words()
    client.publish(
        TopicArn = snsArn,
        Message = msg,
        Subject='A word count statistics'
    )
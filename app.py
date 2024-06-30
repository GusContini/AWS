import boto3
import botocore.config
import json
from datetime import datetime

def using_bedrock(message:str, categories:list)-> str:

    prompt=f"""<s>[INST]Human: Considering the following categories options
    {categories}, categorize the following message: {message}.
    Assistant:[/INST]
    """

    body={
        "prompt": prompt,
        "max_gen_len": 512,
        "temperature": 0.5,
        "top_p": 0.9,
    }

    try:
        bedrock=boto3.client("bedrock-runtime",
                             region_name="us-east-1",
                             config=botocore.config.Config(read_timeout=300,
                                                           retries={
                                                               'max_attempts':3
                                                               }))
        response=bedrock.invoke_model(body=json.dumps(body),
                             modelId="meta.llama3-70b-instruct-v1:0")
        
        response_content=response.get('body').read()
        response_data = json.loads(response_content.decode("utf-8"))
        print(response_data)

        response_detail = response_data['generation']
        
        return response_detail
    
    except Exception as e:
        print(f"Error generating the response: {e}")
        return "~"

def save_message_details_to_s3(s3_key, s3_bucket, original_message, classified_message):
    
    s3=boto3.client('s3')
    current_time = datetime.now().strftime('%Y-%m-%d_%H%M%S')
    message_to_save = f"{current_time}\nOriginal Message: {original_message}\nClassified Message: {classified_message}"

    try:
        s3.put_object(Bucket=s3_bucket, Key=s3_key, Body=message_to_save)
        print("Message saved to s3")
    
    except Exception as e:
        print(f"Error while saving the message to s3: {e}")

def lambda_handler(event, context):
    # TODO implement
    event=json.loads(event['body'])
    message_categ=event['message']
    categories = event['categories']
    generate_message=using_bedrock(message=message_categ, categories=categories)

    if generate_message:
        current_time=datetime.now().strftime('%Y-%m-%d_%H%M%S')
        s3_key=f"message-output/{current_time}.txt"
        s3_bucket='guscontini-aws-bedrock'
        save_message_details_to_s3(s3_key, s3_bucket, message_categ, generate_message)
        response_body = json.dumps({'classified_message': generate_message})

    else:
        print("No message was generated")
        response_body = json.dumps({'error': 'No message was generated'})
    
    return {
        'statusCode': 200,
        'body': response_body
    }

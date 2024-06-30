# Message Classification with AWS Bedrock and AWS Lambda

This serverless application classifies text messages into predefined categories using the power of Amazon Bedrock's foundation models and AWS Lambda.

### Technologies Used

- Amazon Bedrock: Provides access to powerful foundation models (e.g., Llama 2) for natural language processing tasks.

- AWS Lambda: Serverless compute service for running the classification logic.

- AWS API Gateway: Creates a RESTful API endpoint to interact with the Lambda function.

- Boto3: AWS SDK for Python, used to interact with Bedrock and S3.

- Python: Programming language used to implement the Lambda function.
- Amazon S3: Stores the classified messages along with their original content.

### Functionality

1. Receive Message: The application receives a POST request containing a message and a list of possible categories.

2. Invoke Bedrock Model: The Lambda function uses the Bedrock API to invoke a foundation model (e.g., Llama 2) with a prompt designed for text classification.

3. Classify Message: The model analyzes the message and returns the most suitable category from the provided list.

4. Save to S3: The original message and the assigned category are saved to an S3 bucket in a text file.

5. Return Response: The API Gateway returns a JSON response with the classified category.

### API Endpoint

URL: https://iqzolzrrni.execute-api.us-east-1.amazonaws.com/dev/message-classification

Method: POST

Body (JSON):
JSON
{
    "message": "Your message to classify",
    "categories": ["Category1", "Category2", ...]
}

### Usage

1. Prepare Your Request:

- Replace "Your message to classify" with the text you want to classify.

- Replace "Category1", "Category2", etc. with your desired categories.

2. Send POST Request: Use a tool like curl, Postman, or your preferred HTTP client to send a POST request to the API endpoint with the JSON body.

3. Receive Response: The API will respond with a JSON object containing the classified_message key and the assigned category as its value.

Example (using curl):

Bash

curl -X POST -H "Content-Type: application/json" -d '{"message":"This is a test message.", "categories":["Sports", "Technology", "Politics"]}' https://iqzolzrrni.execute-api.us-east-1.amazonaws.com/dev/message-classification

Response Example
JSON
{
    "classified_message": "Technology"
}

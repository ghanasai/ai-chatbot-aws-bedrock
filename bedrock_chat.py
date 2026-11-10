
import boto3

# 1. Connect to Amazon Bedrock
client = boto3.client("bedrock-runtime", region_name="ap-southeast-2")

# 2. Choose which AI model to use
model_id = "amazon.nova-lite-v1:0"

# 3. Create your prompt
messages = [
    {
        "role": "user",
        "content": [{"text": "What is cloud computing? Explain in 2 sentences."}]
    }
]

# 4. Send the message and get a response
response = client.converse(modelId=model_id, messages=messages)

# 5. Extract the text and print it
response_text = response["output"]["message"]["content"][0]["text"]
print(response_text)


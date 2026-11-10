
import os
import boto3

# Connect to Bedrock and choose the model
client = boto3.client("bedrock-runtime", region_name="ap-southeast-2")
model_id = "amazon.nova-lite-v1:0"

# Give the chatbot a personality
system_prompt = [{"text": "You are a friendly cloud computing tutor. Explain concepts simply and use analogies."}]

# Store conversation history
messages = []

print("Chatbot ready! Type 'quit' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit"]:
        print("Goodbye!")
        break

    # Add the user's message to conversation history
    messages.append({"role": "user", "content": [{"text": user_input}]})

    # Send the full conversation to Bedrock with guardrail protection
    response = client.converse(
        modelId=model_id,
        messages=messages,
        system=system_prompt,
        inferenceConfig={
            "temperature": 0.7,
            "topP": 0.9,
            "maxTokens": 512
        },
        guardrailConfig={
            "guardrailIdentifier": os.environ["BEDROCK_GUARDRAIL_ID"],
            "guardrailVersion": "DRAFT",
            "trace": "enabled"
        }
    )

    # Save the response and print it
    assistant_message = response["output"]["message"]
    messages.append(assistant_message)

    print(f"Bot: {assistant_message['content'][0]['text']}")


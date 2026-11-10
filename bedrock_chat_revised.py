
import boto3

# 1. Connect to Bedrock and choose the model
client = boto3.client("bedrock-runtime", region_name="ap-southeast-2")
model_id = "amazon.nova-lite-v1:0"

# 2. Give the chatbot a personality
system_prompt = [{"text": "You are a friendly cloud computing tutor. Explain concepts simply and use analogies."}]

# 3. Store conversation history
messages = []

# 4. Start the conversation loop
print("Chatbot ready! Type 'quit' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit"]:
        print("Goodbye!")
        break

    # 5. Add the user's message to conversation history
    messages.append({"role": "user", "content": [{"text": user_input}]})

    # 6. Send the full conversation to Bedrock
    response = client.converse(
        modelId=model_id,
        messages=messages,
        system=system_prompt,
        inferenceConfig={
            "temperature": 0.1,
            "topP": 0.9,
            "maxTokens": 512
        }
    )

    # 7. Save the response and print it
    assistant_message = response["output"]["message"]
    messages.append(assistant_message)

    print(f"Bot: {assistant_message['content'][0]['text']}")


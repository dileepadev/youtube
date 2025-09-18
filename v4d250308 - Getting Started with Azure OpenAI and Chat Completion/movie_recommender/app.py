import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from colorama import Fore, init

init(autoreset=True)

load_dotenv()

azure_endpoint_from_env = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key_from_env = os.getenv("AZURE_OPENAI_API_KEY")

print(Fore.YELLOW + "Welcome to the Movie Recommendation Chatbot!")
print(Fore.YELLOW + "You can start chatting with the chatbot. Type 'exit' to end the chat.")
print(Fore.BLACK + "-" * 50)

if not azure_endpoint_from_env or not api_key_from_env:
    raise ValueError("Azure OpenAI credentials are missing")

client = AzureOpenAI(
    azure_endpoint=azure_endpoint_from_env,
    api_key=api_key_from_env,
    api_version="2024-08-01-preview",
)

conversation_history = [
    {
        "role": "system",
        "content": "You are a helpful chatbot that recommends movies based on user preferences.",
    },
]

while True:

    user_input = input(Fore.BLUE + "You: ")

    if user_input.lower() == "exit":
        print(Fore.YELLOW + "Exciting the chat. Goodbye!")
        break

    conversation_history.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation_history,
    )

    assistant_response = response.choices[0].message.content

    print(Fore.RED + "Assistant: " + assistant_response)

    conversation_history.append({
        "role": "assistant",
        "content": assistant_response
    })

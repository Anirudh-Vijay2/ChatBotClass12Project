import requests
from colorama import Fore, Style, init

# Initialize colorama (important for Windows)
init(autoreset=True)

# ⚠️ Replace with your NEW OpenRouter API key (never share it!)
API_KEY = "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"

def chat_with_openrouter(messages):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": "gpt-3.5-turbo",  # You can change the model (check openrouter.ai/models)
        "messages": messages
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print(Fore.RED + "Error:", response.status_code, response.text)
        return None


# --- main chatbot loop ---
print(Fore.CYAN + "🤖 OpenRouter Chatbot (type 'exit' to quit)\n")

conversation = [
    {"role": "system", "content": "You are a helpful and friendly assistant."}
]

while True:
    user_input = input(Fore.GREEN + "You: ").strip()
    if user_input.lower() in ["exit", "quit"]:
        print(Fore.YELLOW + "\n👋 Chat ended. Conversation summary:\n")
        for msg in conversation:
            if msg["role"] == "user":
                print(Fore.GREEN + f"🧑 You: {msg['content']}")
            elif msg["role"] == "assistant":
                print(Fore.CYAN + f"🤖 Bot: {msg['content']}")
        break

    conversation.append({"role": "user", "content": user_input})
    reply = chat_with_openrouter(conversation)

    if reply:
        print(Fore.CYAN + f"🤖 Bot: {reply}\n")
        conversation.append({"role": "assistant", "content": reply})


import requests

def chat_with_model(user_input):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": "tinyllama",  # ✅ Use your lightweight model
        "prompt": user_input,
        "stream": False
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        data = response.json()

        # ✅ For generate endpoint, content is returned directly
        return data.get("response", "🤖 (No response from model)")

    except Exception as e:
        return f"⚠️ Error talking to model: {e}"

# Chat loop
print("🤖 Local mahiBot (TinyLLaMA) created by mahidhar: Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("ChatBot: Goodbye!")
        break

    reply = chat_with_model(user_input)
    print("🤖MahiBot:", reply)

from google import genai

API_KEY = "YOUR_API_KEY"


def gemini():
    client = genai.Client(api_key=API_KEY)
    chat = client.chats.create(model="gemini-2.5-flash")

    print('Chatbot is ready. Type "exit" to quit.')
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            break
        response = chat.send_message(user_input)
        print(f"\nGemini: {response.text}")


if __name__ == "__main__":
    gemini()

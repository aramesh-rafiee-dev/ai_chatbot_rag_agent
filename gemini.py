from google import genai
client=genai.Client(api_key="YOUR_API_KEY")
def gemini():
    chat=client.chats.create(
        model="gemini-2.5-flash")
    print("chatbot is ready.for exit write "'exit')
    while True:
        user=input("\nyou:")
        if user.lower()=="exit":
            break
        response= chat.send_message(user)
        print(f"\nGemini:{response.text}")
if __name__=="__main__":
    gemini()


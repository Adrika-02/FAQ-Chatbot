from chatbot import FAQChatbot

def main():
    bot = FAQChatbot("faqs.json")

    print("🤖 FAQ Chatbot (type 'quit' to exit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Bot: Goodbye! 👋")
            break
        response = bot.get_answer(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()

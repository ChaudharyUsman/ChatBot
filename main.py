import openai
openai.api_key = "sk-your-api-key"

def chat_with_gpt(conversation_history):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation_history
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    print("Chatbot is running! Type 'quit' or 'exit' to stop.")
    
    # Initialize conversation history with a system message
    conversation_history = [
        {"role": "system", "content": "You are a helpful assistant. Feel free to ask anything."}
    ]
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye!")
            break

        conversation_history.append({"role": "user", "content": user_input})
        response = chat_with_gpt(conversation_history)
        print("Chatbot:", response)
        conversation_history.append({"role": "assistant", "content": response})

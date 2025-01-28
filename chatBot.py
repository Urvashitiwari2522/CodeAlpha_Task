# Simple chatbot using basic concept of python
def chatbot():
    print("Chatbot: Hi! I'm chatbot. Type 'bye' to exit!")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day!")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I assist you today?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm functioning as expected!")
        elif "your name" in user_input:
            print("Chatbot: I'm a simple Python chatbot. What's your name?")
        elif "what is python" in user_input:
            print("python is a programming language!")
        elif "who are you" in user_input:
            print("i am chatbot!")
        elif "developer name" in user_input:
            print("urvashi")
        else:
            print("Chatbot: Sorry, I don't understand that. Can you rephrase?")

# Run the chatbot
chatbot()
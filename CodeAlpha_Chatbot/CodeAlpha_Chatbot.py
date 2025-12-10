import random

def get_response(user_input):

    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        greetings = ["Hello, how are you"]
        return random.choice(greetings)
    elif "how are you" in user_input:
        return "I am doing good"
    elif "name" in user_input:
        return "I am a chatbot created to assist you"
    elif "help" in user_input:
        return "I can answer simple questions. Try asking something."
    elif "bye" in user_input or "goodbye" in user_input:
        Bye = ["Goodbye! Have a great day ahead. See you later agian"]
        return random.choice(Bye)
    else:
        return"Sorry! could you rephrase it?"
    
def chat():
    #chat function allows looping, that is continuous conversation
    print("Hey user. Iam your friend. Type exit to end the conversation")

    while True:
        
        user_message = input("You:")
        if user_message.lower() =="exit":
            print("Chatbot: Goodbye have a nice day!")
            break
        response = get_response(user_message)
        print("Chatbot:", response)
        
if __name__ == "__main__":
    chat()
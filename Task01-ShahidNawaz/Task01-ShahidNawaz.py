responses = {
    'hello': 'Hi there!',
    'bye': 'Goodbye!',
    'how are you': 'I am doing well, thank you!',
    'name': 'My name is Echo, your rule-based AI chatbot.',
    'help': 'I can respond to greetings, questions, or help commands. Type exit to quit.',
    'weather': 'I cannot check the live weather, but I hope it is sunny where you are!',
}

def get_input():
    
    raw_input = input('You: ')
    return raw_input.lower().strip()

def process(user_input):
    
    reply = responses.get(user_input, 'I do not understand.')
    print(f'Bot: {reply}')


while True:
    user_input = get_input()
    if user_input == 'exit':
        print("Bot: Goodbye!")
        break  
    process(user_input)
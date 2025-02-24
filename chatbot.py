import random
import re

# Define responses with multiple variations
responses = {
    "hello": ["Hello!", "Hi there!", "Hey! How can I help you?", "Hi! Nice to meet you! 😊"],
    "how are you": ["I'm just a bot, but I'm doing great! How about you?", "I'm fine, thanks for asking!"],
    "your name": ["I'm CodeAlphaBot!", "You can call me CodeBot.", "I'm just a chatbot. What’s your name?"],
    "what can you do": ["I can chat with you, answer simple questions, and keep you company!", 
                        "Right now, I can respond to simple messages. Try asking me something!"],
    "who created you": ["I was created by an amazing developer like you!", 
                        "I exist because of passionate coders like you!"],
    "joke": ["Why don’t scientists trust atoms? Because they make up everything! 😆", 
             "Why did the math book look sad? Because it had too many problems. 🤣", 
             "Parallel lines have so much in common. It’s a shame they’ll never meet. 😂"],
    "weather": ["I'm not connected to the internet, but I hope it's sunny where you are! ☀️", 
                "I can't check the weather, but maybe step outside and see?"],
    "favorite color": ["I like all colors! But blue and black look pretty cool. 🎨", 
                       "I don't have eyes, but I bet red is awesome!"],
    "thanks": ["You're welcome! 😊", "No problem! Happy to help.", "Anytime!"],
    "bye": ["Goodbye! Have a great day! 👋", "See you later!", "Bye! Take care!"],
}

# Random fallback responses for unknown inputs
fallback_responses = [
    "I'm not sure how to respond to that. Can you ask something else?",
    "That's interesting! Tell me more.",
    "Hmm... I don’t know much about that, but I'd love to learn!",
    "I'm still learning. Maybe ask me about something else?",
]

# Function to get a response from the chatbot
def get_response(user_input):
    user_input = user_input.lower()

    # Check for a match in predefined responses
    for key in responses:
        if re.search(r'\b' + key + r'\b', user_input):
            return random.choice(responses[key])
    
    # If no match is found, return a fallback response
    return random.choice(fallback_responses)

# Main chatbot loop
print("🤖 Chatbot: Hello! Type 'exit' to end the chat.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("🤖 Chatbot: Goodbye! Have a nice day! 👋")
        break
    response = get_response(user_input)
    print(f"🤖 Chatbot: {response}")

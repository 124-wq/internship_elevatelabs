
print("Hello! I am ChatBot. Let's chat. (type 'bye' to exit)")

while True:
    user_input = input("You: ").lower()  
    if user_input == "bye":
        print("ChatBot: Goodbye! Have a great day!")
        break

    elif "hello" in user_input or "hi" in user_input:
        print("ChatBot: Hello there! How are you?")
    
    elif "how are you" in user_input:
        print("ChatBot: I'm a bot, but I'm doing great! How about you?")
    
    elif "your name" in user_input:
        print("ChatBot: I'm ChatBot, your friendly Python bot.")
    
    elif "time" in user_input:
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"ChatBot: The current time is {current_time}")
    
    elif "weather" in user_input:
        print("ChatBot: I can't check the weather yet, but I hope it's sunny wherever you are!")
    
    elif "joke" in user_input:
        print("ChatBot: Why did the computer go to the doctor? Because it caught a virus!")
    
    else:
        print("ChatBot: Sorry, I didn't understand that. Can you ask something else?")
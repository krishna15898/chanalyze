import random
import datetime
from faker import Faker
fake = Faker()

emojis = ["😄", "😄", "😄", "😄",  # Higher chance of using these
          "😎", "😎",
          "🤔", "🤔",
          "🚀", "🚀",
          "💡", "💡",
          "👍", "👍",
          "🙌", "🙌",
          "😊", "😊",
          "🤩"]

def generate_conversation(num_messages):
    conversation = []
    participants = ["John", "Sarah"]
    
    message_time = fake.date_time_this_year()
    
    for _ in range(num_messages):
        sender = random.choice(participants)
        receiver = [p for p in participants if p != sender][0]
        message = fake.sentence()
        
        if random.random() < 0.25:  # 25% chance of having an emoji
            if len(message.split()) > 2:  # Only add emoji if message is long enough
                words = message.split()
                emoji_index = random.randint(1, len(words) - 1)
                emoji = random.choice(emojis)
                words.insert(emoji_index, emoji)
                message = " ".join(words)
        
        conversation.append(f"{message_time.strftime('%d/%m/%Y, %I:%M %p')} - {sender}: {message}")
        
        message_time += datetime.timedelta(minutes=random.randint(1, 2))
        
        if random.random() < 0.8:  # 80% chance of having a response
            conversation.append(f"{message_time.strftime('%d/%m/%Y, %I:%M %p')} - {receiver}: {fake.sentence()} {random.choice(emojis)}")
            message_time += datetime.timedelta(minutes=random.randint(1, 2))
    
    return "\n".join(conversation)

num_messages = 5000  # Change this to the desired number of messages
conversation_text = generate_conversation(num_messages)

with open("out/chat.txt", "w") as file:
    file.write(conversation_text)

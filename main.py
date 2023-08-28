import emoji
import collections

# Load stopwords
stop = set()
with open("utils/stopwords.txt", 'r') as f:
    for word in f:
        stop.add(word.strip())

# Initialize counters
name1 = "John"
name2 = "Sarah"
ctr1 = collections.Counter()
ctr2 = collections.Counter()
emoji1 = collections.Counter()
emoji2 = collections.Counter()

with open('out/chat.txt', encoding="utf8") as f:
    for line in f:
        parts = line.split(" - ")
        if len(parts) < 2:
            continue
        name, temp = parts[-1].split(": ", maxsplit=1)
        temp = temp.lower()  # Convert to lowercase for consistent comparison

        # Split into individual words or emojis
        tokens = emoji.demojize(temp).split()

        for token in tokens:
            if token.startswith(":") and token.endswith(":"):
                emoji_char = emoji.emojize(token)  # Emojify the emoji_char
                if name == name1:
                    emoji1[emoji_char] += 1
                elif name == name2:
                    emoji2[emoji_char] += 1
            else:
                word = token
                if word not in stop:
                    if name == name1:
                        ctr1[word] += 1
                    elif name == name2:
                        ctr2[word] += 1

# Print most common words and emojis
print("Most common words for", name1 + ":", ctr1.most_common(5))
print("Most common words for", name2 + ":", ctr2.most_common(5))
print("Most common emojis for", name1 + ":", emoji1.most_common(5))
print("Most common emojis for", name2 + ":", emoji2.most_common(5))

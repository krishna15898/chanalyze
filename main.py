import emoji
import collections

# Load stopwords
stop = set()
with open("utils/stopwords.txt", 'r') as f:
    for word in f:
        stop.add(word.strip())

# Initialize counters
emojis = {}
words = {}

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
                if name in emojis:
                    emojis[name][emoji_char] += 1
                else:
                    emojis[name] = collections.Counter(emoji_char)
            else:
                word = token
                if word not in stop:
                    if name in words:
                        words[name][word] += 1
                    else:
                        words[name] = collections.Counter(word)

# Print most common words and emojis
for name in words:
    print("Most common words for", name + ":", words[name].most_common(5))
    print("Most common emojis for", name + ":", emojis[name].most_common(5))

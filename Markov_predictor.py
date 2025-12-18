import re, random
train_data = 'test_text.txt'        
word_after = {}                
pair_after = {}              
def add_to_dict(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = []
    dictionary[key].append(value)

def train_model():
    for line in open(train_data):
        tokens = re.findall(r"[a-zA-Z]+", line.lower())
        n = len(tokens)
        for i, word in enumerate(tokens):
                if i>0:
                    prev = tokens[i - 1] 
                    add_to_dict(word_after, prev, word) 
                if i>1:
                    prev2 = tokens[i - 2] 
                    add_to_dict(pair_after, (prev2, prev), word)
                if i==n-1: 
                    add_to_dict(pair_after, (prev, word), 'END') 
def next_words(context, top_n=3):
    """Return top probable next words."""
    if isinstance(context, str):
        choices = word_after.get(context)
    else:
        choices = pair_after.get(context) 
    if not choices:
        return []
    freq = {}
    for w in choices:
        freq[w] = freq.get(w, 0) + 1
    sorted_words = sorted(freq.items(), key=lambda x: -x[1])
    return [w for w, _ in sorted_words[:top_n]]

train_model()
print("🧠 Markov Next-Word Predictor\n")

sentence = []
while True:
    if not sentence:
        user_input = input("You: ").strip().lower()
        if user_input == "exit":
            break
        tokens = re.findall(r"[a-zA-Z]+", user_input)
        sentence.extend(tokens)
    
    while True:
        if len(sentence) == 1:
            suggestions = next_words(sentence[-1])
        else:
            suggestions = next_words((sentence[-2], sentence[-1]))

        if not suggestions:
            print("🤖 No suggestions. Start new sentence.\n")
            sentence = []
            break

        print("🤖 Suggestions:", ", ".join(suggestions))
        choice = input("Pick one or press Enter for random: ").strip().lower()

        if choice in suggestions:
            next_w = choice
        elif choice == "":
            next_w = random.choice(suggestions)
        else:
            next_w=choice
        sentence.append(next_w)
        print("📝 Sentence so far:", " ".join(sentence), "\n")
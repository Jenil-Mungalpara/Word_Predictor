🧠 Markov Next-Word Predictor
A lightweight Python application that uses Markov Chains to predict and suggest the most likely next word in a sentence. It learns patterns from a training text file and provides real-time suggestions based on bigrams (single word context) and trigrams (two-word context).

🚀 Features
N-gram Language Modeling: Uses 1st-order (one previous word) and 2nd-order (two previous words) Markov chains for context-aware suggestions.
Real-time Learning: Parses local .txt files to build a frequency-based probability dictionary.
Interactive UI: A command-line interface where users can pick suggested words, let the AI choose randomly, or type their own to continue the chain.
Weighted Suggestions: Returns the most probable words first by calculating frequency distributions.

🛠️ Technical Concepts

1. Markov Chains
The core logic relies on the Markov property: the probability of the next word depends only on the current word (or the current pair of words), not the entire history of the conversation.

2. Data Structures
Dictionaries & Lists: The "model" is stored in two dictionaries:
word_after: Maps a single string key to a list of possible following words.
pair_after: Maps a tuple key (word1, word2) to a list of possible following words.
Frequency Sorting: Uses Python's sorted() with a lambda key to identify the "top" suggestions based on how often they appeared in the training data.

3. Regular Expressions (re)
The script uses re.findall(r"[a-zA-Z]+", line.lower()) to:
Normalize text to lowercase.
Strip out punctuation and special characters.
Tokenize the string into a clean list of words.

📂 How It Works
Training: The train_model() function reads test_text.txt line by line.

Mapping: It slides a window across the tokens. If it sees "The cat sat", it adds "cat" to the list of words that follow "the", and "sat" to the list of words that follow the pair ("the", "cat").

Prediction: If you have 1 word, it checks word_after.
If you have 2+ words, it checks pair_after for higher accuracy.

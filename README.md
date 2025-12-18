🧠 Markov Next-Word Predictor
This project is a Python-based word suggestion engine. It uses a Markov Chain model to analyze a text file and predict the most likely words to follow a given input.

📂 Project Components

tempCodeRunnerFile.py: The main script that builds the prediction dictionaries (word_after and pair_after) and runs the interactive loop.


test_text.txt: The training data containing phrases about computer science, Python, and software engineering.

🚀 Features

Dual-Level Context: The model looks at the single previous word or the last two words to find the best suggestion.


Frequency Ranking: Suggestions are sorted so the most common words in the training data appear first.


Interactive Mode: You can pick a suggested word, let the AI choose randomly, or type your own word to build a sentence
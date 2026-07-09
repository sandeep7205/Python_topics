# Define a sentence
sentence = "The quick brown fox jumps over the lazy dog"

# Split the sentence into words
words = sentence.split(" ")

print(words)

# Define a lambda function that checks if a word has more than three letters
has_more_than_three_letters = lambda x: len(x) > 3

# Use the filter function to select words with more than three letters
long_words = list(filter(has_more_than_three_letters, words))

# Print out the list of selected words
print(long_words)

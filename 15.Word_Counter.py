'''
        The function must be named count_words.
        It should accept a single argument: a string of text.
        The returned dictionary should have words as keys and their counts as values.
        Words in the dictionary are case-insensitive ('Word' and 'word' are considered the same).
        Punctuation should be ignored (e.g., 'hello!' and 'hello' are the same word).

        A word that appears in both uppercase and lowercase in the text should be counted as a single word with the sum of both occurrences.
        Any punctuation attached to words should not affect the count.

'''

import string

def count_words(text):
    words = text.lower().split()


    for i in range(len(words)):
        words[i] = "".join([c for c in words[i] if c.isalnum()])

    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


# Example function calls
print(count_words("Hello world! Hello again, world."))  # Should return {"hello": 2, "world": 2, "again": 1}
print(count_words("Unique words only once."))  # Should return {"unique": 1, "words": 1, "only": 1, "once": 1}
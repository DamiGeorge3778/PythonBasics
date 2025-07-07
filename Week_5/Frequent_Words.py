# Q:
# Given a list of words, return the top 3 most frequent words in descending order of frequency.

# Example:
# Input: ["apple", "banana", "apple", "orange", "banana", "apple"]
# Output: ["apple", "banana", "orange"]
# l = ["apple", "banana", "apple", "orange", "banana", "apple"]
from collections import Counter
def frequent_words(words):
    frequency = Counter(words)
    top_3 = frequency.most_common(3)
    return top_3
    
l = ["banana", "apple", "apple", "orange", "banana", "apple"]
print(frequent_words(l))
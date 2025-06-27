# Question 2: Dictionaries
# Given a list of words, write a function that returns a dictionary with the words as keys and their lengths as values.
# Example Input:

# ["apple", "banana", "cherry"]

# Expected Output:

# {'apple': 5, 'banana': 6, 'cherry': 6}

words = ["apple", "banana", "cherry"]
def characters(words):
    d = {}
    for word in words:
        d[word] = len(word)
    return d
print(characters(words))

# 1st iteration
# d = {}
# word = "apple"
# len("apple")
# d = {'apple': 5}

# 2nd iteration
# d = {'apple': 5}
# word = "banana"
# len("banana")
# d = {'apple': 5, 'banana': 6}

# 3rd iteration
# d = {'apple': 5, 'banana': 6}
# word = "cherry"
# len("cherry")
# d = {'apple': 5, 'banana': 6, 'cherry': 6}
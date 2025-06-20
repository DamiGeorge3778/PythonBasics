def count_uppercase(text):
    return sum(1 for char in text if char.isupper())

def count_lowercase(text):
    return sum(1 for char in text if char.islower())

def count_characters(text):
    return len(text)

def count_words(text):
    return len(text.split())

def check_text(text):
    print("Text Analysis Results:")
    print("Uppercase letters:", count_uppercase(text))
    print("Lowercase letters:", count_lowercase(text))
    print("Total characters:", count_characters(text))
    print("Total words:", count_words(text))

user_input = input("Enter a sentence: ")
check_text(user_input)


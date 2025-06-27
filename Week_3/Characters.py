def count_uppercase(text):
    # return sum(1 for char in text if char.isupper())
    u_count = 0
    for character in text:
        if character.isupper():
            u_count += 1
    return u_count
def count_lowercase(text):
    # return sum(1 for char in text if char.islower())
    l_count = 0
    for character in text:
        if character.islower():
            l_count += 1
    return l_count
def count_characters(text):
    # return len(text)
    character_count = 0
    for character in text:
        character_count += 1
    return character_count

def count_words(text):
    # return len(text.split())
    word_count = 0
    for i in text:
        if i == " ":
            word_count += 1
    return word_count + 1
# Text = Good 
# For i in text:
#   print i

def check_text(text):
    print("Text Analysis Results:")
    print("Uppercase letters:", count_uppercase(text))
    print("Lowercase letters:", count_lowercase(text))
    print("Total characters:", count_characters(text))
    print("Total words:", count_words(text))

user_input = input("Enter a sentence: ")
check_text(user_input)


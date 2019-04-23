
inputText = "This is my text, To try things on it so 'i' keep it short as I can :';' !! i can do it"
# .lower() iterate over each char if it is upper convert it to lower
# .upper() iterate over each char if it is lower convert it to upper
out1 = inputText.lower()
out2 = inputText.upper()

from collections import Counter

# manual way
def countWords(text):

    skip = ['.', ',', ':', ';', "'", '"']
    for char in skip:
        text = text.replace(char, "")
    # that is how i remove unwanted chars in my string

    wordsCounter = {}
    for word in text.split():
        if word in wordsCounter:
            wordsCounter[word] += 1
        else:
            wordsCounter[word] = 1
    # now i have a dictionary which the keys is the words i have in my str and value is counter how many times this word appear

    return wordsCounter

# print(countWords(inputText))

# using library collections.Counter which return class object
def countWordsFaster(text):
    text = text.lower()
    skip = ['.', ',', ':', ';', "'", '"']
    for char in skip:
        text = text.replace(char, "")
    # that is how i remove unwanted chars in my string

    wordsCounter = Counter(text.split())
    return wordsCounter

# print(type(countWordsFaster(inputText)))

# samiro0on         # mahmoudsamir109@gmail.com             # 23/03/2019

import re

def reverseChars(inputStr):
    inputList = inputStr.split(" ")
    # print(inputStr)
    outputStr = []
    for items in inputList:
        outputList = []
        for ch in items:
            outputList.append(ch)
        outputList.reverse()
        outputStr.append("".join(outputList))

    outputStr = " ".join(outputStr)
    return outputStr

def mySwapCase(inputStr):
    inputStr = list(inputStr)
    i = 0
    for char in inputStr:
        if char.islower():
            inputStr[i] = char.upper()
        else:
            inputStr[i] = char.lower()
        i+=1
    return ''.join(inputStr)

def stringValidation(inputStr):
    # has any alphanumeric characters
    print(any(char.isalnum() for char in inputStr))
    # has any alphabetical characters
    print(any(char.isalpha() for char in inputStr))
    # has any digits
    print(any(char.isdigit() for char in inputStr))
    # has any lowercase characters
    print(any(char.islower() for char in inputStr))
    # has any uppercase characters
    print(any(char.isupper() for char in inputStr))

def countSubstring(inputString, substring):
    counter = 0
    for index in range(len(inputString) - len(substring) + 1):
        # step = index + len(substring)
        if substring == inputString[index:index + len(substring)]:
            counter += 1
    # or you can use another method
    # counter = inputString.count(substring)
    return counter

def mutateString(inputString, index, char):
    # inputString = inputString[:index] + char + inputString[index+1:]

    stringList = list(inputString)
    stringList[index] = char
    newInputString = ''.join(stringList)

    return newInputString

def changeLetters(inputStr, subString,newSubString):
    newStr = inputStr.replace(subString, newSubString)
    return newStr

def changeLettersUsingRE(inputStr, subString, newSubString):
    newStr = re.sub(subString, newSubString,inputStr)
    return newStr

def removeLetters(inputStr, subString):
    newStr = ''.join([char for char in inputStr if char not in subString])
    return newStr

def reverseString(inputStr):
    newStr = inputStr[::-1]
    return newStr

def firstOccuranceOfSubString(inputStr, subString):
    counter = inputStr.find(subString)
    # if you want the last occarance of the object
    # counter = inputStr.rfind(subString)
    return counter

def formatString():
    string = "Hello, Mr:{} your balance is{:07.3f}$".format("Samir",23.782924)
    # https://www.programiz.com/python-programming/methods/string/format
    return string

def capitaliseFirstLetterInStr(inputStr):
    inputStr = inputStr.split(" ")
    newStr = []
    for word in inputStr:
        newStr.append(word.capitalize())

    # or you can use builtin function title()
    # newStr = inputStr.title()

    return " ".join(newStr)



if __name__ == '__main__':

    str1 = input("please enter a sentence ... ")
    out1 = reverseChars(str1)
    print(out1)
    #######################################################
    # if you wanna swap cases using the built in function
    out2 = out1.swapcase()
    print(out2)
    ########################################################
    # if you wanna swap cases using my implementation
    out3 = mySwapCase(out1)
    print(out3)
    ########################################################
    stringValidation(out1)
    ########################################################
    string = input("please enter your string ... ")
    # .strip()
    sub_string = input("you wanna search for ... ")
    # .strip()
########################################################################################
    # counter = countSubstring(string, sub_string)
    # print("that sub string occur ", counter, " times")

    # out4 = mutateString(out1, 8, 'k')
    # print(out4)

    print(changeLettersUsingRE("myssnamessis mkamoudsssashtsalismilassan", "ss", " "))
    print(changeLetters("myssnamessis mkamoudsssashtsalismilassan", "ss", " "))
    print(removeLetters("myssnamessis mkamoudsssashtsalismilassan", "ss"))
    print(reverseString("batman eats apple !"))
    print(firstOccuranceOfSubString("ncdkc mah saashdmahah msdmhmash mah", "mah"))
    print(formatString())

    print(capitaliseFirstLetterInStr("my name is ay klam !"))
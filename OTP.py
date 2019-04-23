import string
import math
import random


def rand_OTP(sizeOfPW):
    # Takes random choices from
    # ascii_letters and digits
    generate_pass = ''.join([random.choice(string.ascii_uppercase +
                                           string.ascii_lowercase +
                                           string.digits)
                             for nTimes in range(sizeOfPW)])

    return generate_pass

    # Driver Code

password = rand_OTP(10)
print("unique PW is :", password)


def generateOTP():
    # Declare a string variable
    # which stores all string
    str = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    OTP = ""
    length = len(str)
    for i in range(4):
        OTP += string[math.floor(random.random() * 10)]

    return OTP

# pwof6 = generateOTP()
# print(pwof6)
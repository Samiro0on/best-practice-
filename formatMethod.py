# samiro0n              # mahmoudsamir109@gmail.com         # 26/03/2019

# define Person dictionary
person = {'age': 23, 'name': 'Adam', 'country': "UK"}

# format intro
print("{name}'s age is: {age} from {country}".format(**person))


# dynamic string format template
string = "{:{fill}{align}{width}}"

# passing format code as arguments
print(string.format('I Luv Dogs', fill='*', align='^', width=15))

# dynamic float format template
num = "{:{align}{width}.{precision}f}"

# passing format codes as arguments
print(num.format(1239.2367, align='^', width=18, precision=2))

import datetime

# datetime formatting
date = datetime.datetime.now()
print("It's now: {:%Y/%m/%d %H:%M:%S}".format(date))

# applying map and lambda and format methods
num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = list(map(lambda n1, n2: n1+n2, num1, num2))
print("the output of adding two lists using map method to ilterate in lambda nameless function is {}".format(result))


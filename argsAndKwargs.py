
import keyword
print(keyword.kwlist)


def mult(*argv):
    res = None
    for arg in argv:
        if res is None:
            res = arg
        else:
            res *= arg
    return res

out1 = mult(5,7,10)
print(out1)

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("key:%s ==> value:%s" %(key, value))

myFun(start='italy', end="spain", duration= 214)
# **kwargs ---> dictionary
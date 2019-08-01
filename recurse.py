def getFactorial(num):
    if(num == 1) :
        return 1
    return num * getFactorial(num - 1 )


print(getFactorial(5))
print(getFactorial(4))

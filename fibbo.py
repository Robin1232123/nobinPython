fiboList = [1, 1]

fiboIndex = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


for index in fiboIndex:
    temp = fiboList[index - 1] + fiboList[index -2]
    print(temp)
    fiboList.append(temp)


print(fiboList)

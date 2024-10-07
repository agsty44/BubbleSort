list = [7362, 17, 32, 981, 42, 2, 16, 34, 8, 24, 1, 14, 23]
currentNumber = 0
nextNumber = 0
flag = True

#if flag is true, we have made a change
while flag:
    flag = False

    for i in range(len(list) - 1):
        currentNumber = list[i]
        nextNumber = list[i + 1]

        if currentNumber > nextNumber:
            list[i] = nextNumber
            list[i + 1] = currentNumber
            flag = True
print(list)

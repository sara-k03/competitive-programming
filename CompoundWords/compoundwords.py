returnDict = {}

words = []
while True:
    try:
        newWords = input().split(' ')
    except EOFError:
        break
    
    words += newWords

for i in words:
    for j in words:
        if j != i:
            compound = i + j
            returnDict[compound] = 1

returnDict = sorted(returnDict)
for i in returnDict:
    print(i)
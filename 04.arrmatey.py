user = input("Enter a sentence: ")

splitLst = user.split()

index = 0
for i in splitLst:
    print("Argv of ", index, " is ", i)
    index += 1

sortedLst = sorted(splitLst, key=len)

rev = len(sortedLst) - 1

for i in sortedLst:
    print(sortedLst[rev])
    rev -= 1
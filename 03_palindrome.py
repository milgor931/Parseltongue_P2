user = input("Enter text: ")

newLst = []

for i in user:
    if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90):
        newLst.append(i)

shortword = "".join(newLst)

newWord = shortword.lower()
print(shortword)
print(newWord)
rev = ""
backindex = len(shortword) -1

for i in shortword:
    rev += newWord[backindex]
    backindex -= 1

if newWord == rev:
    print("This is a palindrome!")
else:
    print("This is NOT a palindrome!")

#a - z = 97 - 122
#A - Z = 65 - 90
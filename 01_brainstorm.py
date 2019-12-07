import random
lst = ["chimichangas", "chicken nuggets", "kuber's toes", "mila's phone", "sasalele", "little kuber", "stoof", "miwi", "kiwi"]

rnum = len(lst) * random.random()

print(lst[int(rnum)])

answers = []
for i in range(11):
    text = input("Enter a word related to this genre: ")
    answers.append(text)
    print("\t\t\t\t\t\t\t\t" + text)


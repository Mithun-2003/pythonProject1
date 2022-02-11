import string
import random

string1 = string.ascii_lowercase + string.digits + string.ascii_lowercase + string.punctuation
user = int(input("What length would you like your password to be(in numbers): "))
tot1 = []
for i in range(1, user+1):
    random1 = random.choice(string1)
    tot1 += random1
random.shuffle(tot1)
tot2 = ''
for char in tot1:
    tot2 += char
print("Your password: " + tot2)

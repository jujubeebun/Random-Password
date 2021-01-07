import random

letters=["a","b","c","d","e","f","g"]
bletters=["A","B","C","D","E","F","G"]
numbers=[1,2,3,4,5,6,7,8,9]
signs=["!","@","#","$","%"]

password=random.sample(letters, k=2)+random.sample(numbers, k=2)+random.sample(signs, k=2)+random.sample(bletters, k=2)

for i in password:
  print(i, end="")
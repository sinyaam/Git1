import random
output = {}

f = open("characters.txt", 'r')

for i in f:
    number = random.randint(1, 2)
    if number == 1:
        output[i] = ["dead"]
    elif number == 2:
       output[i] = ["alive"]
    
print(output)

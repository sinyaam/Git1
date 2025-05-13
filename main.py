import random
class Char():
    def __init__(self):
        self.alive = random.choice([True, False])
a = []
f = open("characters.txt", 'r')

for i in f:
    a.append(i)
    
print(a)

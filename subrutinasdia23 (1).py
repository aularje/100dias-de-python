import random
def rollDice(i):
    dado = random.randint(1,6)
    print(f"{i}. Haz lanzado ", dado)
    
for i in range(1, 101):
    rollDice(i)
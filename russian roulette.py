import time
import random
import os
print("It's russian roulette boys!")
y = int(input("Clip size:"))
x = random.randrange(1, y, 1)
bullet = random.randrange(1, y, 1)
print("It's your turn")
time.sleep(random.randrange(3, 5))
if x == bullet:
    print("ed shot")
else:
    print("You win...for this time")
os.system("pause")

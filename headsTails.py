import sys
print("Heads = 1")
print("Tails = 2")
coinFlip = int(input("Heads or Tails: "))

if coinFlip == 1:
    print("You picked heads.")
elif coinFlip == 2:
    print("You picked tails.")
else:
    print("Enter a vaild number next time.")
    sys.exit()

import random
nagu = (random.randint(1,2))

if nagu == 1:
    print("It landed on heads.")
elif nagu == 2:
    print("It landed on tails.")

if coinFlip == nagu:
    print("Beta, you are lucky ducky.")
else:
    print("Beta, you suck.")

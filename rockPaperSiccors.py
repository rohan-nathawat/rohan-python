import sys
import random
print("Rock = 1")
print("Paper = 2")
print("Scissors = 3")
uNum = int(input("Rock, Paper, Scissors: "))
cNum = random.randint(1,3)

if uNum == 1:
    print("You picked Rock.")
elif uNum == 2:
    print("You picked Paper.")
elif uNum == 3:
    print("You picked Scissors.")
else:
    print("Enter a vaild number next time.")
    sys.exit()

if cNum == 1:
    print("Computer picked Rock.")
elif cNum == 2:
    print("Computer picked Paper.")
else:
    print("Computer picked Scissors.")


if uNum == 1 and cNum == 1:
    print("Tie")
elif uNum == 1 and cNum == 2:
    print("Lose")
elif uNum == 1 and cNum == 3:
    print("Win")
elif uNum == 2 and cNum == 1:
    print("Win")
elif uNum == 2 and cNum == 2:
    print("Tie")
elif uNum == 2 and cNum == 3:
    print("Lose")
elif uNum == 3 and cNum == 1:
    print("Lose")
elif uNum == 3 and cNum == 2:
    print("Win")
elif uNum == 3 and cNum == 3:
    print("Tie")
else:
    print("No one can see this...")
print ('''This program will tell you 
if a number you enter is divisble
by 2, 3, or both''')
dNum = input ("Enter a number: ")
fNum = float(dNum)

if fNum % 6 == 0:
    print("The number is divisble by 2 and 3")
elif fNum % 3 == 0:
    print("The number is divisble by 3")
elif fNum % 2 == 0:
    print("The number is divisble by 2")
else:
    print("Your number is not divisble")

import random
k = random.randint (-100, 100)

found = False

while found == False:

  l = int(input("Enter a number:  "))

  if k==l: 
    found = True
    print("You figured it out!")
  elif k>l:
    print(str(l), "is more then that")
  elif k<l:
    print(str(l), "is less then that")
  else:
    print("Sorry try again :) ")
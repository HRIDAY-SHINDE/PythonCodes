import random
print("guessing no. game")
a=random.randint(1,20)
chances=0
print("guess a no. between 1 to 20")
while (chances<4):
    b=int(input("guess a no.: "))
    if b==a:
        print("you won!!!")
        break
    elif b<a:
        print("select a higher no.")
    elif b>a:
        print("select a lower no.")
    else:
        print("error")
    chances=chances+1
if not chances<4:
    print("you lose. the no. was: ", a)



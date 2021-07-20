import secrets

count=0
while (count<3 | count>(-2)):
    c = str(input("Make your choice: stone/paper/scissor-- "))
    a = ['stone', 'paper', 'scissor']
    computer = secrets.choice(a)
    if (c==computer):
       print("computer: ",computer)
       print("its a tie")
       count=count+0
       print("your points", count)
    elif (computer=="stone" and c=="paper"):
       print("computer: ",computer)
       print("you win")
       count=count+1
       print("your points", count)
    elif (computer=="scissor" and c=="paper"):
       print("computer: ",computer)
       print("you lose")
       count=count-1
       print("your points", count)
    elif (computer=="stone" and c=="scissor"):
       print("computer: ",computer)
       print("you lose")
       count=count-1
       print("your points", count)
    elif (computer=="paper" and c=="stone"):
       print("computer: ",computer)
       print("you lose")
       count=count-1
       print("your points", count)
    elif (computer=="scissor" and c=="stone"):
       print("computer: ",computer)
       print("you won")
       count=count+1
       print("your points", count)
    elif (computer=="paper" and c=="scissor"):
       print("computer: ",computer)
       print("you win")
       count=count+1
       print("your points", count)
    elif count<(-1) :
             
           break 
    elif count==3:
    
            break
    else:
        print("error")


    
    

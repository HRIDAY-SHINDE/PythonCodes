def add(a,b):
    result= a+b
    print("a+b=",result)
def sub(a,b):
    result= a-b
    print("a-b=",result)
def div(a,b):
    result= a/b
    print("a/b=",result)    
def mult(a,b):
    result= a*b
    print("a*b=",result)
a = int(input("Type First no. for operation:"))
b = int(input("Type Second no. for operation:"))
c = input("Type symbol of operation:")
if c=="+":
    add(a,b)
elif c=="-":
    sub(a,b)    
elif c=="*":
    mult(a,b)          
elif c=="/":
    div(a,b)
else:
    print("Invalid")

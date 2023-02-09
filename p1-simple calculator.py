#simple calculator
def add(a,b):
    c=a+b
    return c

def sub(a,b):
    c=a-b
    return c

def mul(a,b):
    c=a*b
    return c

def div(a,b):
    if(a>b):
        c=a/b
    else:
        a,b=b,a
        c=a/b
    return c
a=eval(input())
b=eval(input())
i = 0
j = 1
while(j):
    print("enter your choice:\n1 is add\n2 is sub\n3 is mul\n 4 is div\n:")
    ch=int(input())
    if(ch==1):
        c=add(a,b)
        print(c)
        i = i + 1
    elif(ch==2):
        c=sub(a,b)
        print (c)
        i = i + 1
    elif(ch==3):
        c=mul(a,b)
        print (c)
        i = i + 1
    elif(ch==4):
        c=div(a,b)
        print (c)
        i = i + 1
    else:
        j = 0
print("No of times the loop executed : " , i)
a = "* "
print(a * 3)

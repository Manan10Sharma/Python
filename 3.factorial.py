num=int(input("enter a number:"))
f=1
if num<0:
    print("sorry,invalid entry")
elif num==0:
    print("factorial:1")
else:
    for i in range(1,num+1):
        f=f*i
    print("factorial of",num,"is",f)

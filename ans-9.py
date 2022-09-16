#Write a python script to calculate LCM of two numbers
n1=int(input("enter first number: "))
n2=int(input("enter second number: "))
max=n1 if n1>n2 else n2
while 1:
    if max%n1==0 and max%n2==0:
        print("LCM is: ",max)
        break
    max+=1    

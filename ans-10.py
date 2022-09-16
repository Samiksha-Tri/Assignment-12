#Write a python script to calculate HCF of two numbers
hcf=0
n1=int(input("enter first number : "))
n2=int(input("enter second number : "))
max=n1 if n1>n2 else n2
for i in range(2,max+1):
    if n1%i==0 and n2%i==0:
        hcf=i
print("HCF : ",hcf)      
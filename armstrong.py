n=int(input("Enter number:- "))
count=0
temp=n
num=temp
sum=0
while(n!=0):
    r=n%10
    n=n//10
    count+=1
while(temp!=0):
    rm=temp%10
    temp=temp//10
    sum=sum+rm**count
if(sum==num):
    print("Number is armstrong.")
else:
    print("number is armstrong.")
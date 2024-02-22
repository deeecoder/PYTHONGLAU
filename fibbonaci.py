n=int(input("Enter range:- "))
a=0
b=1
print(a)
sum=0
for i in range(2,n):
    a=b
    b=sum
    sum=a+b
    print(sum)

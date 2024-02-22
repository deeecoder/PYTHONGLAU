n=int(input("Enter list size:- "))
l=[]
sum=0
for i in range(0,n):
    l.append(int(input("Enter value:- ")))
    sum+=l[i]
print("Sum of all elements of a list:- ",sum)
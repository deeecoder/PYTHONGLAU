n=int(input("Enter size:- "))
l=[]
for i in range(0,n):
    l.append(int(input("Enter elements:- ")))
temp=l[0]
l[0]=l[n-1]
l[n-1]=temp
print(l)
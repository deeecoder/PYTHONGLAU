n=int(input("Enter size:- "))
l=[]
max=0
for i in range(0,n):
    l.append(int(input("Enter elements:- ")))
    if(max<l[i]):
        max=l[i]
print("Maximum element in list",max)
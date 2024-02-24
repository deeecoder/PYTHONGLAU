n=int(input("Enter size:- "))
l=[]
l1=[]
for i in range(0,n):
    l.append(int(input("Enter elements:- ")))
    if l[i] not in l1:
        l1.append(l[i])
print(l1)
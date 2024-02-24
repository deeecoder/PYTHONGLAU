n=int(input("Enter size:- "))
l=[]
l_even=[]
l_odd=[]
for i in range(0,n):
    l.append(int(input("Enter elements: ")))
    if(i%2==0):
        l_even.append(l[i])
    else:
        l_odd.append(l[i])
print("Elements at even index: ",l_even)
print("Elements at odd index: ",l_odd)

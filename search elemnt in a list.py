n=int(input("Enter size:- "))
l=[]
for i in range(0,n):
    l.append(int(input("Enter elements:- ")))
element=int(input("Enter elemnt to find:- "))
for j in range(0,n):
    if(element==l[j]):
        position=j
print("Element found at position:-",position)


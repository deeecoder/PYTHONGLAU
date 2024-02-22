n=int(input("Enter number:- "))
temp=n
rev=0
while(n!=0):
    r=n%10
    n=n//10
    rev=rev*10+r
if(temp==rev):
    print("Number is palindrome.")
else:
    print("Number is not palindrome.")

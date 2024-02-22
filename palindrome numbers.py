n=int(input('Enter Number'))
temp=n
rev=0
while n!=0:
    r=n%10
    n=n//10
    rev=rev*10+r
if rev==temp:
    print('Number is palindrome')
else:
    print('Number is not palindrome')
    

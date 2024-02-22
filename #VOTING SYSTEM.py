#VOTING SYSTEM
name=str(input("Enter you name:- "))
age=int(input("Enter your age:- "))
voting_id=str(input("Enter voter id no:- "))
if age>18:
    print("Candidate is eligible for voting.")
    vote=int(input("1.BJP\n2.SP\n3.AAP\nEnter your vote:-"))
    if vote==1:
        print("voted for BJP")
    elif vote==2:
        print("Voted for SP")
    elif vote==3:
        print("Voted for AAP")
else:
    print("Candidate is not eligible for voting.")

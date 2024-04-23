# Function to cast a vote
def cast_vote(votes, candidate):
    if candidate in votes:
        votes[candidate] += 1
    else:
        print(f'Error: {candidate} is not a valid candidate')

# Function to tally the votes
def tally_votes(votes):
    total_votes = 0
    for candidate, count in votes.items():
        total_votes += count
        print(f'{candidate}: {count} votes')
    print(f'Total votes: {total_votes}')

# Get the candidates from the user
candidates = input('Enter the candidates (separated by commas): ').split(',')

# Create an empty dictionary to store the votes
votes = {}

# Add the candidates to the dictionary
for candidate in candidates:
    votes[candidate.strip()] = 0

# Cast some votes
cast_vote(votes, 'BJP')
cast_vote(votes, 'CNG')
cast_vote(votes, 'TMC')
cast_vote(votes, 'AAP')
cast_vote(votes, 'RJD')

# Tally the votes
tally_votes(votes)
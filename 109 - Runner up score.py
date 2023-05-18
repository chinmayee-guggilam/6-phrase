'''Given the participants' score sheet for your University Sports Day, you are 
required to find the runner-up score. You are given scores. Store them in a 
list and find the score of the runner-up.
If the following string is given as input to the program:
5
2 3 6 6 5
Then, the output of the program should be:
5'''
#Code
# Get the number of participants from the user
n = int(input("Enter the number of participants: "))

# Get the scores from the user
scores = list(map(int, input("Enter the scores: ").split()))

# Remove duplicates and sort the scores in descending order
unique_scores = sorted(set(scores), reverse=True)

# The runner-up score is the second highest score
runner_up_score = unique_scores[1]

# Print the runner-up score
print("Runner-up score:", runner_up_score)

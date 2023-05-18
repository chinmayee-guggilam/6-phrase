'''You are given words. Some words may repeat. For each word, output its 
number of occurrences. The output order should correspond with the input 
order of appearance of the word. See the sample input/output for 
clarification.
If the following string is given as input to the program:
4
bcdef
abcdefg
bcde
bcdef
Then, the output of the program should be:
3
2 1 1'''
#Code
# Get the number of words
n = int(input())

# Initialize an empty dictionary to store word counts
word_counts = {}

# Process each word
for _ in range(n):
    word = input()
    # Increment the count of the word in the dictionary
    word_counts[word] = word_counts.get(word, 0) + 1

# Output the word counts in the order of appearance
for count in word_counts.values():
    print(count, end=' ')

'''Write a program to compute the frequency of the words from the input. 
The output should output after sorting the key alphanumerically.
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or
Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1'''
#Code
def compute_word_frequency(sentence):
    words = sentence.split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    sorted_frequency = sorted(frequency.items(), key=lambda x: x[0])

    return sorted_frequency

if __name__ == "__main__":
    # Input the sentence
    sentence = input("Enter a sentence: ")

    # Compute the word frequency
    frequency = compute_word_frequency(sentence)

    # Output the word frequency
    for word, count in frequency:
        print(f"{word}:{count}")
#Output
'''Enter a sentence: Python is a new software that is ruling the it world python software is trending
Python:1
a:1
is:3
it:1
new:1
python:1
ruling:1
software:2
that:1
the:1
trending:1
world:1'''

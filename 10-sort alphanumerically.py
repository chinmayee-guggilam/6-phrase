'''Write a program that accepts a sequence of whitespace separated words as
input and prints the words after removing all duplicate words and sorting
them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world'''
#Code:
phrase = input("Type in: ")
phrase_splited = phrase.split(' ')

word_list = []
for i in phrase_splited:
    if i not in word_list:
        word_list.append(i)
    else:
        continue
word_list.sort()
print((' ').join(word_list))
#Output:
'''Type in: hello world and practice makes perfect and hello world again
again and hello makes perfect practice world'''


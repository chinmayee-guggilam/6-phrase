'''Write a program that accepts a sentence and calculate the number of
letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3'''
#Code:
phrase = input("Type in: ")
phrase = list(phrase)

l, d = 0, 0
for i in phrase:
    if i.isalpha():
        l = l + 1
    if i.isdigit():
        d = d + 1
    else:
        pass

print("Letters:", l)
print("Digits:", d)
#Output:
'''Type in: hello world!123
Letters: 10
Digits: 3'''

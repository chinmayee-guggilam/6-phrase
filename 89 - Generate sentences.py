'''Please write a program to generate all sentences where subject is in ["I", 
"You"] and verb is in ["Play", "Love"] and the object is in 
["Hockey","Football"].'''
#Code
subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]

# Generate all sentences
sentences = []
for subject in subjects:
    for verb in verbs:
        for obj in objects:
            sentence = subject + " " + verb + " " + obj
            sentences.append(sentence)

# Print all sentences
for sentence in sentences:
    print(sentence)

#Output
'''
I Play Hockey
I Play Football
I Love Hockey
I Love Football
You Play Hockey
You Play Football
You Love Hockey
You Love Football
'''

'''You are required to write a program to sort the (name, age, score) tuples 
by ascending order where name is string, age and score are numbers. The 
tuples are input by console. The sort criteria is:
o 1: Sort based on name
o 2: Then sort based on age
o 3: Then sort by score
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom',
'19', '80')]'''
#Code
def sort_tuples(tuples):
    sorted_tuples = sorted(tuples, key=lambda x: (x[0], int(x[1]), int(x[2])))
    return sorted_tuples


if __name__ == "__main__":
    # Input the tuples
    tuples = []
    while True:
        input_str = input("Enter a tuple (name, age, score) or press Enter to stop: ")
        if input_str == "":
            break
        else:
            tuple_values = input_str.split(",")
            tuples.append(tuple_values)

    # Sort the tuples
    sorted_tuples = sort_tuples(tuples)

    # Output the sorted tuples
    print(sorted_tuples)
#Output
'''Enter a tuple (name, age, score) or press Enter to stop: Tom,19,80
Enter a tuple (name, age, score) or press Enter to stop: John,20,90
Enter a tuple (name, age, score) or press Enter to stop: Jony,17,91
Enter a tuple (name, age, score) or press Enter to stop: Jony,17,93
Enter a tuple (name, age, score) or press Enter to stop: Json,21,85
Enter a tuple (name, age, score) or press Enter to stop: 
[['John', '20', '90'], ['Jony', '17', '91'], ['Jony', '17', '93'], ['Json', '21', '85'], ['Tom', '19', '80']]'''

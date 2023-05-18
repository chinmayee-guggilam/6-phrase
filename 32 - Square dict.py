'''Define a function which can print a dictionary where the keys are numbers 
between 1 and 20 (both included) and the values are square of keys'''
#Code
def print_square_dict():
    square_dict = {num: num ** 2 for num in range(1, 21)}
    for key, value in square_dict.items():
        print(f"Key: {key}, Value: {value}")
print_square_dict()

#Output
'''Key: 1, Value: 1
Key: 2, Value: 4
Key: 3, Value: 9
Key: 4, Value: 16
Key: 5, Value: 25
Key: 6, Value: 36
Key: 7, Value: 49
Key: 8, Value: 64
Key: 9, Value: 81
Key: 10, Value: 100
Key: 11, Value: 121
Key: 12, Value: 144
Key: 13, Value: 169
Key: 14, Value: 196
Key: 15, Value: 225
Key: 16, Value: 256
Key: 17, Value: 289
Key: 18, Value: 324
Key: 19, Value: 361
Key: 20, Value: 400'''

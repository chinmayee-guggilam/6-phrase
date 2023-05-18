'''Write a function to compute 5/0 and use try/except to catch the 
exceptions'''
#Code
def compute_division():
    try:
        result = 5 / 0
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero")
    except Exception as e:
        print("Error:", e)

# Call the function
compute_division()

#Output
'''
Error: Division by zero
'''

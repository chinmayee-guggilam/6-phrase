'''Python has many built-in functions, and if you do not know how to use it, 
you can read document online or find some books. But Python has a built-in 
document function for every built-in functions.
Please write a program to print some Python built-in functions documents, 
such as abs(), int(), raw_input()
And add document for your own function'''
#Code
# Print documentation for built-in functions
print("Documentation for abs():")
print(help(abs))
print("")

print("Documentation for int():")
print(help(int))
print("")

print("Documentation for input():")
print(help(input))
print("")

# Define a custom function with documentation
def greet(name):
    """
    This function greets the person with the given name.

    Parameters:
    name (str): The name of the person to greet.

    Returns:
    str: The greeting message.
    """
    return f"Hello, {name}! Nice to meet you."

# Print documentation for the custom function
print("Documentation for greet():")
print(help(greet))

#Output
'''Documentation for abs():
Help on built-in function abs in module builtins:

abs(x, /)
    Return the absolute value of the argument.

None

Documentation for int():

None

Documentation for input():
Help on built-in function input in module builtins:

input(prompt='', /)
    Read a string from standard input.  The trailing newline is stripped.
    
    The prompt string, if given, is printed to standard output without a
    trailing newline before reading input.
    
    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
    On *nix systems, readline is used if available.

None

Documentation for greet():
Help on function greet in module __main__:

greet(name)
    This function greets the person with the given name.
    
    Parameters:
    name (str): The name of the person to greet.
    
    Returns:
    str: The greeting message.

None'''

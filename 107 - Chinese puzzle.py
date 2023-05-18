'''Write a program to solve a classic ancient Chinese puzzle: We count 35 
heads and 94 legs among the chickens and rabbits in a farm. How many 
rabbits and how many chickens do we have?'''
#Code
def solve_puzzle(heads, legs):
    for c in range(heads + 1):
        r = heads - c
        if (2 * c + 4 * r) == legs:
            return c, r
    return None

# Define the total number of heads and legs
total_heads = 35
total_legs = 94

# Solve the puzzle
solution = solve_puzzle(total_heads, total_legs)

# Print the solution
if solution:
    chickens, rabbits = solution
    print("Number of chickens:", chickens)
    print("Number of rabbits:", rabbits)
else:
    print("No solution found.")

#Output
'''
Number of chickens: 23
Number of rabbits: 12
'''

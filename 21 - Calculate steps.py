'''A robot moves in a plane starting from the original point (0,0). The robot 
can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace 
of robot movement is shown as the following:
 UP 5
DOWN 3
LEFT 3
Six Phrase – mySlate – Python Session Plan
RIGHT 2
The numbers after the direction are steps. Please write a program to 
compute the distance from current position after a sequence of movement 
and original point. If the distance is a float, then just print the nearest 
integer. Example: If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2'''
#Code
import math

def calculate_distance(movements):
    x = 0
    y = 0

    for movement in movements:
        direction, steps = movement.split()
        steps = int(steps)

        if direction == "UP":
            y += steps
        elif direction == "DOWN":
            y -= steps
        elif direction == "LEFT":
            x -= steps
        elif direction == "RIGHT":
            x += steps

    distance = math.sqrt(x**2 + y**2)
    nearest_distance = round(distance)

    return nearest_distance

if __name__ == "__main__":
    # Input the movements
    movements = []
    while True:
        input_str = input("Enter a movement (direction steps) or press Enter to stop: ")
        if input_str == "":
            break
        else:
            movements.append(input_str)

    # Calculate the distance
    distance = calculate_distance(movements)

    # Output the distance
    print(distance)
#Output
'''Enter a movement (direction steps) or press Enter to stop: UP 5
Enter a movement (direction steps) or press Enter to stop: DOWN 3
Enter a movement (direction steps) or press Enter to stop: LEFT 3
Enter a movement (direction steps) or press Enter to stop: RIGHT 2
Enter a movement (direction steps) or press Enter to stop: 
2'''

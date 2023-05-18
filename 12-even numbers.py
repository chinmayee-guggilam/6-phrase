'''Write a program, which will find all such numbers between 1000 and 3000
(both included) such that each digit of the number is an even number.The
numbers obtained should be printed in a comma-separated sequence on a
single line.'''
#Code:
numbers = []
for x in range (1, 1001):
    numSplit = [int(d) for d in str(x)]
    odd = False
    for y in range (0, len(numSplit)):
        if numSplit[y] % 2 != 0:
            odd = True
    if (odd == False):
        numbers.append(x)
print (numbers)
#Output:
'''[2, 4, 6, 8, 20, 22, 24, 26, 28, 40, 42, 44, 46, 48, 60, 62, 64, 66, 68,
 80, 82, 84, 86, 88, 200, 202, 204, 206, 208, 220, 222, 224, 226, 228,
 240, 242, 244, 246, 248, 260, 262, 264, 266, 268, 280, 282, 284, 286,
 288, 400, 402, 404, 406, 408, 420, 422, 424, 426, 428, 440, 442, 444,
 446, 448, 460, 462, 464, 466, 468, 480, 482, 484, 486, 488, 600, 602,
 604, 606, 608, 620, 622, 624, 626, 628, 640, 642, 644, 646, 648, 660,
 662, 664, 666, 668, 680, 682, 684, 686, 688, 800, 802, 804, 806, 808,
 820, 822, 824, 826, 828, 840, 842, 844, 846, 848, 860, 862, 864, 866,
 868, 880, 882, 884, 886, 888]'''

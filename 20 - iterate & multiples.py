'''Define a class with a generator which can iterate the numbers, which are 
divisible by 7, between a given range 0 and n.'''
#Code
class DivisibleBySeven:
    def __init__(self, n):
        self.n = n

    def divisible_by_seven_generator(self):
        for num in range(self.n + 1):
            if num % 7 == 0:
                yield num
n =int(input())
divisible = DivisibleBySeven(n)
generator = divisible.divisible_by_seven_generator()

for num in generator:
    print(num)
#Output
'''67
0
7
14
21
28
35
42
49'''



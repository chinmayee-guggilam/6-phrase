'''Define a class named American and its subclass NewYorker'''
#Code
class American:
    pass

class NewYorker(American):
    pass

# Example usage
person1 = American()
person2 = NewYorker()

print(isinstance(person1, American))    
print(isinstance(person1, NewYorker))  

print(isinstance(person2, American))   
print(isinstance(person2, NewYorker))

#Output
'''
True
False
True
True
'''

'''Define a class Person and its two child classes: Male and Female. All 
classes have a method "getGender" which can print "Male" for Male class and 
"Female" for Female class.'''
#Code
class Person:
    def getGender(self):
        print("Unknown")

class Male(Person):
    def getGender(self):
        print("Male")

class Female(Person):
    def getGender(self):
        print("Female")
male = Male()
female = Female()

male.getGender()   # Output: Male
female.getGender() # Output: Female

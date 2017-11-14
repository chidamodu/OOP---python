#Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
class Person:
    gender="Transgender"
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
    def getGender(self):
        print("Gender is {}".format(self.gender))

class Male(Person):
    def __init__(self):
        data={"gender":"Male"}
        super().__init__(**data)

class Female(Person):
    def __init__(self):
        data={"gender":"Female"}
        super().__init__(**data)

# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
class Strg:
    def __init__(self):
        self.s=""
    def getString(self):
        self.s=input("Please input your string to print:")
    def printString(self):
        print(self.s.upper())

gh=Strg()
gh.getString()

#Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
class Numb:
    def __init__(self):
        self.n=int
    def getinp(self):
        self.n=int(input("Would you like to play with numbers? Why wait?"))
    def divisible_num(self):
        res=(self.n for self.n in range(self.n) if (self.n % 7)==0)
        for i in res:
            print(i)

# Define a class, which have a class parameter and have a same instance parameter.
class Person:
    def __init__(self, name=None):
        self.name=name
        if self.name != None:
            print(self.name)

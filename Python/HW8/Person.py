#Person.py  test class


class Person:
    def __init__(self, fname, lname ):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

class Student(Person):
    def __init__(self, fname, lname, year):
        Person.__init__(self, fname, lname)
        #super().__init__(fname, lname) inherits all the parents methods and properties
        self.student_id = None
        self.graduation = year



x = Student("Joe", "Blow", 2019)
x.printname()

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


florist = Person("Jane", "Flowers")
florist.printname()


class Lawyers(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        # self.firstname = fname
        # self.lastname = lname

    def printinfo(self):
        print(self.firstname, self.lastname)


happy_lawyers = Lawyers("Jack", "Smiley")
happy_lawyers.printname()

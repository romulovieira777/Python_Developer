class Instructors:
    companyName = "Bluelime"

    def __init__(self, course):
        self.course = course

    def printinfo(self):
        print("My Company name is", Instructors.companyName)


elearning = Instructors("Python for beginners")

bls = Instructors("Django for beginners")

bls.printinfo()

print(bls.course)

# multiple_inheritance.py

class Father:
    def skills(self):
        print("Father: Driving")

class Mother:
    def skills(self):
        print("Mother: Cooking")

class Child(Father, Mother):
    def talents(self):
        print("Child: Playing guitar")


c = Child()

c.skills()     # Which one runs?
c.talents()

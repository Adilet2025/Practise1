class Student:
    # Class variable (shared by all students)
    school = "KBTU"

    def __init__(self, name):
        # Instance variable (belongs to each object)
        self.name = name

    @classmethod
    def show_school(cls):
        # cls refers to the class (Student)
        print("School:", cls.school)

    def show_name(self):
        # self refers to the object
        print("Name:", self.name)


# Create objects
s1 = Student("Ali")
s2 = Student("Dana")

# Call instance method (works with object data)
s1.show_name()
s2.show_name()

# Call class method (works with class data)
Student.show_school()

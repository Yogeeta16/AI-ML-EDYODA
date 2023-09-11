class Student:

    def __init__(self):
        # private properties
        self.__name = ""
        self.__rollNumber = ""

# methods : set name value to the private property
    def setName(self, name):
        self.__name = name

# methods : get name value to the private property
    def getName(self):
        return self.__name

# methods : set rollnumber value to the private property
    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

# methods : get rollnumber value to the private property
    def getRollNumber(self):
        return self.__rollNumber


student1 = Student()
student1.setName("Lily")
student1.setRollNumber("06")

print("Name:", student1.getName())
print("Roll Number:", student1.getRollNumber())


student2 = Student()
student2.setName("Riya")
student2.setRollNumber("01")

print("Name:", student2.getName())
print("Roll Number:", student2.getRollNumber())

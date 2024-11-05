class Student:
    #PRoperties/Variables/Attributes/Characteristics
    name = "Nina"
    gender = "Female"
    age = 30

    #Behaviors/Method/Function
    def study(self):
        print("Student is studying")

#Object1
student1 = Student()    #Creating an object
student1.study()
print(student1.name)

#Object2
student2 = Student()

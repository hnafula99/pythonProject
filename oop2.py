class Person:
    def __init__(self, name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age

    def movement(self):
        print("Person is walking")

person1 = Person(name:"Nina", gender:"Female", age:30)
print(person1.name)

person2 = Person(name:"Lyka",gender:"Female", age:1)
print(person2.name)

person3 = Person(name:"Lyka",gender:"Female", age:1)
print(person3.name)
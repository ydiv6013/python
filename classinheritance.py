# A Python program to demonstrate inheritance

class Person :
    #constructor
    def __init__(self ,name,id):
        self.name = name
        self.id = id

    def getName(self):
        return self.name

    def getId(self):
        return self.id
    
    def isEmployee(self):
        return False
    def display(self):
        print(self.name,self.id)

# Class Employee inherit all the attributes and methods of class Person
class Employee (Person):
    def __init__(self, name, id,salary,post):
        super().__init__(name, id)
        self.salary =salary
        self.post =post

    def display(self):
        super().display()
        print(self.salary)
        print(self.post)
  
    def isEmployee(self):
        return True


person = Person("Yogesh",102)
print(person.getName(),person.getId(),person.isEmployee())
person.display()

employee =Employee("Hiren",103,15000,"Sales Manager")
print(employee.getName(),employee.getId(),employee.isEmployee())
employee.display()
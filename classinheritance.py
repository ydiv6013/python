# A Python program to demonstrate inheritance

class Person :

    master_key ="6013"
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

    def getSalary(self):
        return self.salary
    
    def display(self):
        super().display()
        print(self.salary)
        print(self.post)
  
    def isEmployee(self):
        return True

class Student(Employee):
    def __init__(self, name, id, salary, post,age,dob):
        super().__init__(name, id, salary, post)
        self.age =age
        self.dob = dob

    def getAge(self):
        return self.age
    
    def getDob(self):
        return self.dob
    
    def display(self):
        super().display()
        print(self.age)
        print(self.dob)

class Mother():
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    
    def display(self):
        print(f"mother's name is {self.name} and her age is {self.age}")
        
class Father():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    
    def display(self):
        print(f"father's name is {self.name} and his age is {self.age}")


class Parents(Father,Mother):
    def __init__(self,name,age):
        super().__init__(name,age)
    
    
person = Person("Yogesh",102)
print(person.getName(),person.getId(),person.isEmployee())
person.display()

employee =Employee("Hiren",103,15000,"Sales Manager")
print(employee.getName(),employee.getId(),employee.isEmployee())
employee.display()
print(f"salary of {employee.getName()} is {employee.getSalary()}")

student = Student("Mohit",104,20000,"Manager",26,"05/05/1993")
student.display()
print(f"salary of {student.getName()} is {student.getSalary()}")
print(f"Dob of {student.getName()} is {student.getDob()}")
print(f"Age of {student.getName()} is {student.getAge()}")
print(student.master_key)
father = Father("Rameshbhai",58)
mother = Mother("Devkuvarben" , 59)
parents = Parents("Hina",56)
mother.display()
father.display()

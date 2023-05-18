# employee master program will create a employee txt file.
email_list = []
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
    
    def __init__(self, name, id,salary,age,email):
        super().__init__(name, id)
        self.salary =salary
        self.age =age
        self.email = email 
        

    def getSalary(self):
        return self.salary
    
    def display(self):
        super().display()
        print(self.salary)
        print(self.age)

    def insertFile(self):
        record = self.name + "," + self.id + ","+ self.salary + "," + self.age + ","+ self.email + "|" + "\n"
        with open("employee.txt" , 'a') as file :
            file.write(record)
       
    def getEmail(self):

        with open("employee.txt") as file :
            content = file.read()
            line = content.split('|')
            
            for x in line :
                try:
                    value= x.split(',')
                    print(value[4])
                except:
                    print("No more record found")
                
    def isEmployee(self):
        return True
    

#name = input("Please enter your name : ")
#emp_id = input("Please enter your employee id : ")
#salary = input("Please enter your currant salary : ")
#age = input("Please enter your current age : ")
#email = input("please enter your email id : ")
employee = Employee("a",12,234,45,"a@vn.com")
#employee = Employee(name,emp_id,salary,age,email)
#employee.display()
#employee.insertFile()
employee.getEmail()
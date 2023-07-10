students = [    
    { 
        'name': 'Alice',
        'age': 20,
        'major': 'Computer Science',
        'gpa': 3.8    
    },    
    {        
        'name': 'Bob',        
        'age': 21,        
        'major': 'Business',        
        'gpa': 3.5    
    },    
    {        
        'name': 'Charlie',        
        'age': 19,        
        'major': 'Mathematics',        
        'gpa': 3.9   
    },    
    {        
        'name': 'David',        
        'age': 22,        
        'major': 'Engineering',        
        'gpa': 3.2   
    }]


name = input("enter your name")
age = int(input("enter your age"))
major =input("enter your major")
gpa = float(input("enter your gpa"))

def add_record(name,age,major,gpa):
    students_name = name
    students_age = age
    students_major = major
    students_gpa = gpa

    new_students ={}
    new_students["name"] = students_name
    new_students["age"] = students_age
    new_students["major"] = students_major
    new_students["gpa"] = students_gpa
    students.append(new_students)
    print(new_students)
    print(students)

    
add_record(name,age,major,gpa)

for key in students:
    print(f"name : {key['name']}")
    print(f"age : {key['age']}")
    print(f"major : {key['major']}")
    print(f"gpa : {key['gpa']}")


for name in students:
    print(name['name'])
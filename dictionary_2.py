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

for key in students:
    print(f"name : {key['name']}")
    print(f"age : {key['age']}")
    print(f"major : {key['major']}")
    print(f"age : {key['gpa']}")
      
for name in students:
    print(name['name'])
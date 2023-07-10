print("Welcome to the pythons student grading program")


# Creates a empty dictionary
student_grade = {
    'Alice': 92,
    'Bob': 87,
    'Charlie': 65,
    'David': 78,
    'Emma': 55
}



for key in student_grade:
    print(key)
    grade = int(student_grade[key])
    print(grade)

    if grade > 90 :
        student_grade[key]="Outstanding"
    elif grade > 80 :
        student_grade[key]="Exceeds Expectation"
    elif grade > 70 :
        student_grade[key]="Acceptable"
    elif grade > 60 :
        student_grade[key]="Average"
    else :
        student_grade[key]="Fail"

print(student_grade)
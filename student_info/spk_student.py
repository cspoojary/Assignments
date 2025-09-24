
n=int(input("Enter number of students: "))
students={}     
for i in range(n):
    name=input(f"Enter name of student {i+1}: ")
    marks=[]
    for j in range(3):
        mark=int(input(f"Enter marks in subject {j+1}: "))
        marks.append(mark)
    total=sum(marks)
    average=total/3
    if average >= 90:
        grade='A'
    elif average >= 80:
        grade='B'
    elif average >= 70:
        grade='C'
    elif average >= 60:
        grade='D'
    else:
        grade='F'
    students[name]={'marks':marks,'total':total,'average':average,'grade':grade}
print("\nStudent Details:")
for name, details in students.items():
    print(f"Name: {name}")
    print(f"Marks: {details['marks']}")
    print(f"Total: {details['total']}")
    print(f"Average: {details['average']:.2f}")
    print(f"Grade: {details['grade']}\n")
    
    
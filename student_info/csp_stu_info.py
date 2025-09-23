#Student Report Program

number_student = int(input("Enter number of the students: "))
students = []

for i in range(number_student):
    name = input(f"\nEnter name of the student {i+1}: ")
    marks = []
    for j in range(1,4):
        while True:
            mark = int(input(f"Enter marks for subject {j}(0-100): "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else: 
                print("Highest mark is 100, So add between 0 to 100")




    total = sum(marks)
    avg = total / len(marks)


    #Grade logic
    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    elif avg >= 40:
        grade = "D"
    else:
        grade = "F"

    students.append({
        "name": name,
        "marks":marks,
        "total":total,
        "average": avg,
        "grade": grade
    })


    print("\n======STUDENT REPORT=======\n")
    for s in students:
        print(f"Name: {s['name']}")
        print(f"Marks: {s['marks']}")
        print(f"Total: {s['total']}")
        print(f"Average: {s['average']:.2f}")
        print(f"Grade: {s['grade']}\n")
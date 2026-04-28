class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        self.students.append(name)

    def count_students(self):
        return len(self.students)



room = Classroom()

while True:
    print("\n1. Add Student")
    print("2. Count Students")
    print("3. Exit")

    i= int(input("Choose an option: "))

    if i == 1:
        name = input("Enter student name: ")
        room.add_student(name)
        print(f"{name} added successfully.")


    elif i == 2:
        print("Total students:", room.count_students())

    elif i == 3:
        print("Exit")
        break
    
    else:
        print("Invalid choice, try again.")
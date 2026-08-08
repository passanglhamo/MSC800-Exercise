#This class add the student details and sort according to age
class Student_Details:

    def __init__(self, name, age, address,student_id):
        self.name = name
        self.age = age
        self.address = address
        self.student_id = student_id
        self.students = []

    #This method adds the student details (You can add multiple students)
    def get_student(self):
        while True:
            student_info = input(
                "Enter student name,age,address,student_id: "
            ).split(',')

            if len(student_info) != 4:
                print("Please enter name,age,address and student id.")
                continue

            name, age, address, student_id = student_info

            self.students.append(
                Student_Details(
                    name,
                    int(age),
                    address,
                    int(student_id)
                )
            )

            choice = input("Do you want to add another student? (yes/no): ").lower()

            if choice != "yes":
                break
    #This method display the student details (As per the age in ascending order).
    # The sorting used is bubble sort algorithm.
    def sort_students_by_age(self):
        n=len(self.students)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.students[j].age > self.students[j+1].age:
                    self.students[j], self.students[j+1] = self.students[j+1], self.students[j]
        print("Students sorted by age:")
        for student in self.students:
            print(f"Name: {student.name}, Age: {student.age}, Address: {student.address}, Student ID: {student.student_id}")            

if __name__ == "__main__":
    student_details = Student_Details("",0,"",0)
    student_details.get_student()
    student_details.sort_students_by_age()
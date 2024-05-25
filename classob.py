class Student:
    def __init__(self):
        self.subject1 = 0
        self.subject2 = 0
        self.subject3 = 0
    
    def input_marks(self):
        self.subject1 = int(input("Enter marks for subject 1: "))
        self.subject2 = int(input("Enter marks for subject 2: "))
        self.subject3 = int(input("Enter marks for subject 3: "))
    
    def calculate_result(self):
        total_marks = self.subject1 + self.subject2 + self.subject3
        average_marks = total_marks / 3
        
        if self.subject1 >= 35 and self.subject2 >= 35 and self.subject3 >= 35 and average_marks >= 40:
            return "Pass"
        else:
            return "Fail"

if __name__ == "__main__":
    student = Student()
    student.input_marks()
    result = student.calculate_result()
    print("Result:", result)
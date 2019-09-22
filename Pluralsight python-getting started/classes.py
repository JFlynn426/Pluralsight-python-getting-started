students =[]

class Student:
   
    school_name = "Springfield Elementary"

    def __init__(self, name, student_id=0):
        student = { "name": name, "student_id": student_id}
        self.name -name
        self.student_id = student_id
        students.append(name)

    def get_name_capitalize(self):
        return self.get_name_capitalize.capitalize()

    def get_school_name(self):
        return self.school_name

    def __str__(self):
        return "Student " +self.name

mark = Student("Mark")

print(students)
    
class HighSchoolStudent(Student):
    
    school_name = "Springfield High School"

    def get_school_name(self):
        return "This is a High School Student"

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "HS"

    


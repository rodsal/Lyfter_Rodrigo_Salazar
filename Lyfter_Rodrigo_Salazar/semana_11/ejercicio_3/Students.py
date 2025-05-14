import actions

class Students(): 
    def __init__(self):
        self.students = []
        
    
    def add_student(self, student):
        self.students.append(student)
        

    def display_all_students(self):
        for student in self.students:
            student.display_student_info()
            print("---------------------------------")
    
    def calculate_students_average(self):
        averages_per_student = {}
        for student in self.students:
            average = 0
            sum_grades = student.spanish_grade + student.english_grade + student.ss_grade + student.science_grade
            average = actions.calculate_average(sum_grades)
            averages_per_student[student.name] = average
        return averages_per_student
    
    def convert_to_dictionary (self):
        students_to_dic = []
        for student in self.students:
            students_to_dic.append({
                "nombre_completo": student.name,
                "section": student.section,
                "nota_español": student.spanish_grade,
                "nota_ingles": student.english_grade,
                "nota_estudios_sociales": student.ss_grade,
                "nota_ciencias": student.science_grade
                })
        return students_to_dic

    def convert_from_dictionary(self,dic_students):
        for dic_student in dic_students:
            new_student = actions.request_student_dictionary(dic_student)
            self.add_student(new_student)


class Student():
    def __init__(self,name,section,spanish_grade,english_grade,ss_grade,science_grade):
        self.name = name
        self.section = section
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.ss_grade = ss_grade
        self.science_grade = science_grade

    def display_student_info(self):
        print("Nombre: " + self.name)
        print("Sección: " + self.section)
        print("Nota de español: " + str(self.spanish_grade))
        print("Nota de ingles: " + str(self.english_grade))
        print("Nota de Estudios Sociales: " + str(self.ss_grade))
        print("Nota de ciencias: " + str(self.science_grade))
        

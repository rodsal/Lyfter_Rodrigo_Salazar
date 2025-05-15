class Employee():
    def __init__(self, name, employee_ID):
        self.name = name
        self.employee_ID = employee_ID
    
    def show_employee_info(self):
        print ("Nombre: " + self.name + "\nNúmero de Empleado: " + str(self.employee_ID))

class Developer():
    def __init__(self, languages):
        self.languages = languages
    
    def programing_languages(self):
        print("Lenguajes: " + ", ".join(self.languages))

class Designer ():
    def __init__(self, tools):
        self.tools = tools
    
    def design_tools(self):
        print("Herramientas: " + ", ".join(self.tools))

class EmpleadoHibrido(Employee, Developer,Designer):
    def __init__(self, name, employee_ID, languages, tools):
        Employee.__init__(self, name, employee_ID)
        Developer.__init__(self, languages)
        Designer.__init__(self, tools)
    
    def show_hybrid_employee(self):
        self.show_employee_info()
        self.programing_languages()
        self.design_tools()

    def hybrid_employee_seniority(self):
        if len(self.languages) <= 1 and len(self.tools) <= 1:
            print("El empleado es nivel junior")
        elif len(self.languages) <= 1 and len(self.tools) > 1 or len(self.languages) > 1 and len(self.tools) <= 1:
            print("El empleado es nivel mid")
        elif len(self.languages) > 1 and len(self.tools) > 1:
            print("El empleado es nivel senior")


empleado_h = EmpleadoHibrido("Rodrigo", 2203,["python","java"],["adobe","figma"])
empleado_h.show_hybrid_employee()
empleado_h.hybrid_employee_seniority()







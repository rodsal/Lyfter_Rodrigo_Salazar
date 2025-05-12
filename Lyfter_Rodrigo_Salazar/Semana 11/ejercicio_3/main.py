import menu
import data
from Students import Students

students = Students()
continue_running,students_array = data.initialize_values()
while(continue_running):
    #try:
        menu.show_menu()
        selected_option = menu.read_option()
        continue_running = menu.option_execution(selected_option,students)

    #except Exception as general_exception:
    #    print("Una excepción ocurrió: " + str(general_exception))
    #    continue_running = False        

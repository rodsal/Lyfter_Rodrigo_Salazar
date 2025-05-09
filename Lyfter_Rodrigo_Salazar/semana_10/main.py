import menu
export_path = "students_data_export.csv"
continue_running = True
students = []
while(continue_running):
    try:
        menu.show_menu()
        selected_option = menu.read_option()
        continue_running, students = menu.option_execution(selected_option, export_path,students)

    except Exception as general_exception:
        print("Una excepcin ocurrió: " + str(general_exception))
        continue_running = False        

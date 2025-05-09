import menu
path = "students_data.json"
continue_running = True
while(continue_running):
    #try:
    menu.show_menu()
    selected_option = menu.read_option()
    continue_running = menu.option_execution(selected_option, path)

    #except Exception as general_exception:
    #    print("An excpetion occured: " + str(general_exception))
    #    continue_running = False        

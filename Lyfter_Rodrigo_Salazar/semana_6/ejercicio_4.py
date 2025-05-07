def revert_text(text):
    reversed_string = ""
    for index in range(len(text) -1,-1,-1):
        reversed_string = reversed_string + text[index]
    return reversed_string

string_to_reverse = "Hola mundo"
print(revert_text(string_to_reverse))
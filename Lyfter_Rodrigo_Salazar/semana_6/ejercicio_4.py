def revert_text(text):
    reversed_string = ""
    if isinstance(text, str):
        for index in range(len(text) -1,-1,-1):
            reversed_string = reversed_string + text[index]
    else:
        raise TypeError ("The value inputted is not a text value ")
    return reversed_string
 
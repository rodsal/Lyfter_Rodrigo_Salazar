def print_upper_lower_cases(text):
    lower_count = 0
    upper_count = 0
    if isinstance(text, str):
        for word in text.replace(" ",""):
            if word.isupper():
                upper_count += 1
            else:
                lower_count += 1
    else: 
        raise TypeError ("The value inputted is not a text value ")
    return lower_count, upper_count


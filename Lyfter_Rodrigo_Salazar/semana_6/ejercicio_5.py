def print_upper_lower_cases(text):
    lower_count = 0
    upper_count = 0
    for word in text.replace(" ",""):
        if word.isupper():
            upper_count += 1
        else:
            lower_count += 1
    return lower_count, upper_count

text_to_validate = "I lovE NacióN Sushi"
print(print_upper_lower_cases(text_to_validate))
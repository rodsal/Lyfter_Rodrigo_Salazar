def order_text_by_alphabet (text):
    text_splitted = text.split("-")
    text_splitted.sort()
    text_ordered = ""
    for index in range(len(text_splitted)):
        if index != 0:
            text_ordered = text_ordered + "-" + text_splitted[index]
        else:
            text_ordered = text_ordered + text_splitted[index]
    return text_ordered

text_to_order = "python-variable-funcion-computadora-monitor"
print(order_text_by_alphabet(text_to_order))
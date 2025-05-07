grade_counter = 0
approved_grades_qunatity = 0
disapprove_grade_quantity = 0
approved_grades_percentage = 0
disapprove_grade_percentage = 0
total_grades_percenatge = 0

grades_quantity = int(input("Ingrese la cantidad de notas: "))
while grade_counter < grades_quantity:
    grade_counter = grade_counter + 1
    actual_grade = int(input("Ingrese la nota numero " + str(grade_counter) + ": "))
    if actual_grade < 70:
        disapprove_grade_quantity = disapprove_grade_quantity + 1
        disapprove_grade_percentage = disapprove_grade_percentage + actual_grade
    else:
        approved_grades_qunatity = approved_grades_qunatity + 1
        approved_grades_percentage = approved_grades_percentage + actual_grade
    total_grades_percenatge = total_grades_percenatge + (actual_grade/grades_quantity)

if disapprove_grade_quantity > 0:
    disapprove_grade_percentage = disapprove_grade_percentage/disapprove_grade_quantity
if approved_grades_qunatity > 0:
    approved_grades_percentage = approved_grades_percentage/approved_grades_qunatity

print("El estudiante tiene esta cantidad de notas aprobadas: " + str(approved_grades_qunatity))
print("El promedio de las notas aprobadas: " + str(approved_grades_percentage))

print("El estudiante tiene esta cantidad de notas desaprobadas: " + str(disapprove_grade_quantity))
print("El promedio de las notas desaprobadas: " + str(disapprove_grade_percentage))   

print("Este es el primedio total de notas: " + str(total_grades_percenatge))
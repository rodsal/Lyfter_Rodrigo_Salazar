"""
2. Analice los siguientes algoritmos usando la Big O Notation:
"""
# print_numbers_times_2
def print_numbers_times_2(numbers_list):
	for number in numbers_list: # O(n)
		print(number * 2)		# O(1)
# Big O notation = O (n)

#check_if_lists_have_an_equal
def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a:           # O(n)
		for element_b in list_b:	   # O(n)
			if element_a == element_b: # O(1)
				return True			   # O(1)
				
	return False					   # O(1)
# Big O notation = O(n^2)

#print_10_or_less_elements
def print_10_or_less_elements(list_to_print): 
	list_len = len(list_to_print)			  # O(1)
	for index in range(min(list_len, 10)):    # O(1)
		print(list_to_print[index])           # O(1)

# Big O notation = O(1)


#generate_list_trios
def generate_list_trios(list_a, list_b, list_c):
	result_list = []                            							# O(1)                         
	for element_a in list_a:												# O(n)
		for element_b in list_b:											# O(n)
			for element_c in list_c:										# O(n)
				result_list.append(f'{element_a} {element_b} {element_c}')  # O(1)
				
	return result_list 														# O(1)

# Big O notation = O(n^3)




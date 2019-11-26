"""
Виконати обробку елементів прямокутної матриці A, що має n рядків і m
стовпців. Виключити з матриці рядок з номером k. Зімкнути рядки матриці.
"""
import re
import numpy

pattern=re.compile(r"[+]?\d+$")

def fill_array(number_rows, number_columns):
	array_form_list = [[int(number_validator(pattern, "\nВведіть елемент " + str(y+1) + " рядка, " + str(x+1) + " cтовпця : ")) for x in range (number_columns)] for y in range(number_rows)] 
	return array_form_list

def validator(pattern, prompt):
	data=input(prompt)
	while not bool(pattern.match(data)):
		print("\nУвага! Ви ввели неправильне значення !")
		data=input(prompt)
	return int(data)

def number_validator(pattern, prompt):
	number=validator(pattern, prompt)
	while (number<=0):
		print("\nУвага! Ви ввели неправильне числове значення !")
		number=validator(pattern, prompt)
	return number

def row_validator(pattern, prompt, number_rows):
	number=validator(pattern, prompt)
	while((number<=0) or (number>number_rows)):
		print("\nУвага! Ви ввели неправильне числове значення !")
		number=validator(pattern, prompt)
	return number

def init():
	print("\nЗавдання 2: Виконати обробку елементів прямокутної матриці A, що має n рядків і m "+
		  "стовпців. Виключити з матриці рядок з номером k. Зімкнути рядки матриці.")

def start2():
	init()
	number_rows=number_validator(pattern, "\nВведіть кількість рядків масиву : ")
	number_columns=number_validator(pattern, "\nВведіть кількість стовпців масиву : ")
	while(number_columns==number_rows):
		print("\nУвага! Кількість стовпців не може дорівнювати кількості рядків!")
		number_columns=number_validator(pattern, "\nВведіть кількість стовпців масиву : ")

	how_to_enter_data=str(input("\nДля ручного введення даних натисніть Enter, будь-що інше для автоматичного заповнення масиву "))

	if(how_to_enter_data==''):
		not_final_numbers=fill_array(number_rows, number_columns)
		numbers=numpy.array(not_final_numbers)
	else:
		numbers=numpy.random.randint(0,1001,(number_rows, number_columns))

	print("\nПочатковий вигляд масиву з " + str(number_rows) + " рядками та " + str(number_columns) + " стовпцями : ")
	print(numbers)

	row_to_eliminate=row_validator(pattern, "\nВведіть рядок, який потрібно видалити : ", number_rows)

	numbers=numpy.delete(numbers, row_to_eliminate-1, 0)
	print("\nМасив після видалення " + str(row_to_eliminate) + " рядка : ")
	print(numbers)
	
	numbers=numbers.flatten('C')
	print("\nВигляд масиву із зімкнутими рядками : ")	
	print(list(numbers))	




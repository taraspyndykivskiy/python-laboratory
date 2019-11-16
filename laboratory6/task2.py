"""
Виконати обробку елементів прямокутної матриці A, що має n рядків і m
стовпців. Виключити з матриці рядок з номером k. Зімкнути рядки матриці.
"""
import re
import numpy

pattern=re.compile(r"[+]?\d+$")

def validator(pattern, prompt):
	data=input(prompt)
	while not bool(pattern.match(data)):
		data=input(prompt)
	return int(data)

def number_validator(pattern, prompt):
	number=validator(pattern, prompt)
	while (number<=0):
		number=validator(pattern, prompt)
	return number

def row_validator(pattern, prompt, number_rows):
	number=validator(pattern, prompt)
	while((number<0) or (number>number_rows-1)):
		number=validator(pattern, prompt)
	return number

def init():
	print("\nЗавдання 2: Виконати обробку елементів прямокутної матриці A, що має n рядків і m "+
		  "стовпців. Виключити з матриці рядок з номером k. Зімкнути рядки матриці.")

def start2():
	init()
	number_rows=number_validator(pattern, "\nВведіть кількість рядків масиву : ")
	number_columns=number_validator(pattern, "\nВведіть кількість стовпців масиву : ")

	numbers=numpy.random.randint(0,1001,(number_rows, number_columns))
	print("\nПочатковий вигляд масиву з " + str(number_rows) + " рядками та " + str(number_columns) + " стовпцями : ")
	print(numbers)

	row_to_eliminate=row_validator(pattern, "\nВведіть рядок, який потрібно видалити : ", number_rows)

	numbers=numpy.delete(numbers, row_to_eliminate, 0)
	print("\nМасив після видалення " + str(row_to_eliminate) + " рядка : ")
	print(numbers)
	
	numbers=numbers.flatten('C')
	print("\nВигляд масиву із зімкнутими рядками : ")	
	print(numbers)




import re
import array
import random

pattern=re.compile(r"[+-]?\d+$")

def init():
	print("\nЗавдання 1: Дано одновимірний масив числових значень, що нараховує n елементів. "+ 
		  "Виключити з масиву елементи, що належать проміжку [b;c].")

def number_validator(prompt, pattern):
	number=int(validator(prompt, pattern))
	while number<=0:
		number=int(validator(prompt, pattern))
	return number

def validator(prompt, pattern):
	data=(input(prompt))
	while not bool(pattern.match(data)):
		data=(input(prompt))
	return data


def start1():
	init()
	number_elements=number_validator("\nВведіть розмірність початкового масиву : ", pattern)

	numbers=array.array('q', [random.randrange(0, 1001, 1) for i in range(number_elements)])
	final_numbers=array.array('q',[i for i in numbers])

	print("\nПочатковий масив з числами : ")
	print(list(numbers))

	start_point=number_validator("\nВведіть мінімальне значення проміжку : ", pattern)
	finish_point=number_validator("\nВведіть максимальне значення проміжку : ", pattern)

	for element in numbers:
		if (element>=start_point) and (element<=finish_point):
			final_numbers.remove(element)

	print("\nФінальний масив з числами, які не входять у проміжок [ " + str(start_point) + " ; " + str(finish_point) + " ]")
	print(list(final_numbers))



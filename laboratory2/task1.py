"""
Обчислити значення знака суми (i=0,1,2, .... , n), де x^i - елемент, шо сумується
"""
import math 
import re

pattern_x=re.compile(r"^[+-]?[0-9]*\.?[0-9]*$|")
pattern_number=re.compile(r"^[+]?[0-9]*$|")

def init():
	print("\nЛабораторна робота №2 \nПиндиківський Тарас, КМ-93")
	print("16 варіант")
	print("Завдання 1: обчислення значення знака суми")

def validator(pattern, prompt):
    text = input(prompt)
    while not bool(pattern.findall(text)[0]):
        text = input(prompt)
    return text


def x_validator(prompt):

	number = float(validator(pattern_x, prompt))
	while (not number) and (number!=0):
	    number = float(validator(pattern_x, prompt))
	return number

def final_iteration_number_validation(prompt):

	number = int(validator(pattern_number, prompt))
	while not number:
	    number = int(validator(pattern_number, prompt))
	return number

def main():
		sum=0
		i=0

		final_iteration_number=final_iteration_number_validation("\nВведіть натуральне значення числа n : ")
		x=x_validator("\nВведіть довільне значення числа х : ")
	
		for i in range(final_iteration_number):
			sum+=pow(x,(i+1))

		print("\nЗначення суми дорівнює : " + str(sum))



init()
main()





















"""
Дано ціле число N(>0). Знайти найменше ціле додатне число K,
квадрат якого перевершує N: K2 > N.
Функцію добування квадратного кореня не використовувати.
"""

import math 
import re

#natural_pattern=re.compile(r"^[+]?[0-9]*$|")
natural_pattern=re.compile(r"^[+]?\d*$|")

def validator(pattern, prompt):
    text = input(prompt)
    while not bool(pattern.findall(text)[0]):
        text = input(prompt)
    return text

def natural_number_validator(prompt):

	number = int(validator(natural_pattern, prompt))
	while not number:
	    number = int(validator(natural_pattern, prompt))
	return number

def init():
	print("\nЛабораторна робота №2 \nПиндиківський Тарас, КМ-93")
	print("16 варіант")
	print("Завдання 2: визначення найменшого цілого числа, квадрат якого перевищує n.")

def main():

	n=natural_number_validator("\nВведіть натуральне значення N : ")

	initial_number=1

	while(pow(initial_number, 2)<=n):
		initial_number+=1

	print("\nНайменше додатнє ціле число, квадрат якого перевищує "+str(n)+" дорівнює "+str(initial_number)+" ( "+str(pow(initial_number,2))+ " ) ")

init()
main()




























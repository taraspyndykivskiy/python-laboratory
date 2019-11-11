"""
Визначити чи точка А(х,у) належить графіку квадратичної функції із коефіцієнтами a, b, c (y = a*x^2 + b*x + c)
"""
import math 
import re

pattern=re.compile(r"^[-]?[0-9]*\.?[0-9]*$|")
def init():
	print("\nЛабораторна робота №1 \nПиндиківський Тарас, КМ-93")
	print("16 варіант\n")
	print("Завдання 2: визначення приналежності точки графіку квадратичної функції\n")
	print("Для визначення квадратичної функції виду y = a*x^2 + b*x + c\n" )

def validator(pattern, prompt):
    text = input(prompt)
    while not bool(pattern.findall(text)[0]):
        text = input(prompt)
    return text


def coefficient_validator(prompt):

	number = float(validator(pattern, prompt))
	while (not number) and (number!=0):
	    number = float(validator(pattern, prompt))
	return number



def main():
	a=coefficient_validator("\nведіть коефіцієнт а : ")
	b=coefficient_validator("\nВведіть коефіцієнт b : ")
	c=coefficient_validator("\nВведіть коефіцієнт c : ")

	x=coefficient_validator("\nВкажіть координату х точки А : ")
	y=coefficient_validator("\nВкажіть координату y точки А : ")

	print("\n")


	if(y==(a*pow(x,2)+b*x+c)):
		print("Точка А з координатами: ( "+str(x)+" ; "+str(y)+" )"+" належить графіку функції y = "+str(a)+"*x^2 "+"+ "+str(b)+"*x"+" + "+str(c))
	else:
		print("Точка А з координатами: ( "+str(x)+" ; "+str(y)+" )"+" не належить графіку функції y = "+str(a)+"*x^2 "+"+ "+str(b)+"*x"+" + "+str(c))

init()
main()
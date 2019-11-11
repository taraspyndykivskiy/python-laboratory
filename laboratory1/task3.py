"""
Обчислити значення конкретної функції, в залежності від введеного аргументу : 
f(x)=x^4+9, якщо x<3.2
f(x)=(54*x^4)/(-5*x^2+7), якщо x>=3.2
"""
import math 
import re

pattern=re.compile(r"^[+-]?[0-9]*\.?[0-9]*$|")

def validator(pattern, prompt):
    text = input(prompt)
    while not bool(pattern.findall(text)[0]):
        text = input(prompt)
    return text


def x_validator(prompt):

	number = float(validator(pattern, prompt))
	while (not number) and (number!=0):
	    number = float(validator(pattern, prompt))
	return number
def init():
	print("\nЛабораторна робота №1 \nПиндиківський Тарас, КМ-93")
	print("16 варіант\n")
	print("Завдання 3: обчислення значення функції в залежності від значення х\n")

def main():
	x=x_validator("Введіть значення аргументу x : ")
	if(x<3.2):
		function=pow(x, 4)+9
	elif(x>=3.2):
		function=(54*pow(x,4))/(-5*pow(x, 2)+7)
	print("\n")
	print("F ( "+str(x)+" ) = "+str(function))

init()
main()
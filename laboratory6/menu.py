#D:\Taras Pyndykivskiy\kpi\programming\programming_1\laboratory_works\6"""
import re
from task1 import start1
from task2 import start2
pattern=re.compile(r"[+]?\d{1}$")
print("\nЛабораторна робота №6 \nПиндиківський Тарас, КМ-93")
print("16 варіант")


def number_validator(prompt, pattern):
	number=int(validator(prompt, pattern))
	while ((number!=1) and (number!=2)):
		number=int(validator(prompt, pattern))
	return number

def validator(prompt, pattern):
	data=(input(prompt))
	while not bool(pattern.match(data)):
		data=(input(prompt))
	return data

cont=input("\nНатисніть Enter, щоб продовжити, будь-що інше, щоб завершити роботу з програмою ")
while cont=='':
	task_number=number_validator("\nВведіть номер програми задачі для запуску її виконання (1/2) : ", pattern)
	if(task_number==1):
		start1()
	elif(task_number==2):
		start2()
	cont=input("\nНатисніть Enter, щоб продовжити, будь-що інше, щоб завершити роботу з програмою ")

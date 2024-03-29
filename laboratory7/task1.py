#D:\Taras Pyndykivskiy\kpi\programming\programming_1\laboratory_works\#7
"""
Є текстовий файл.
Надрукувати:
 його перший рядок;
 його п'ятий рядок;
 його перші 5 рядків;
 його рядки з s1-го по s2-ий;
 весь файл.
"""
import sys
import re

pattern=re.compile(r"^[+]?\d+$")

def init():
	print("\nЛабораторна робота №7 \nПиндиківський Тарас, КМ-93")
	print("16 варіант")
	print("Завдання 1: Вивести вміст файлу")

def validator(pattern, prompt):
	data=input(prompt)
	while not bool(pattern.match(data)):
		print("\nУвага! Ви ввели неправильне значення !")
		data=input(prompt)
	return data

def start_line_validator(pattern, prompt, number_lines):
	
	number=int(validator(pattern, prompt))
	while ((number<=0) or (number>number_lines-1)):
		print("\nУвага! Ви ввели неправильне значення !")
		number=int(validator(pattern, prompt))

	return number

def finish_line_validator(pattern, prompt, start_line_to_print, number_lines):
	number=int(validator(pattern, prompt))
	while ((number<=start_line_to_print) or  (number>number_lines)):
		print("\nУвага! Ви ввели неправильне значення !")
		number=int(validator(pattern, prompt))

	return number
	
init()
cont=''
CGREEN='\033[32m'
CCYAN='\033[36m'
CEND='\033[0m'
CRED='\033[91m'

while cont=='':
	cont=input("\nНатисніть Enter, щоб продовжити, будь-що інше, щоб завершити роботу з програмою ")
	if(cont!=''): 
		break

	try:
		file=open("task1.py", 'r', encoding = "utf-8")
	except FileNotFoundError:
		print("Вказаного файлу не існує")
		sys.exit()

	number_lines=0 

	while True:
		s = file.readline()
	#	print(s)
		number_lines+=1
		if not s:
			break

	file.close()

	number_lines-=1
	print(number_lines)
	file=open("task1.py", 'r', encoding = "utf-8")
	if number_lines<5:
		print("\nУ Вашому файлі менше 5 рядків")
		sys.exit()

	file_lines = [line.strip() for line in file]

	print(CRED + "\nПерший рядок файлу : " + CEND)
	print(file_lines[0])

	print(CRED + "\nП'ятий рядок файлу : " + CEND)
	print(file_lines[4])

	print(CRED + "\nПерші 5 рядків файлу" + CEND)
	for i in range(5):
		print(file_lines[i])

	print('\n')
	start_line_to_print=start_line_validator(pattern, "\nВведіть початковий номер рядка файлу : ", number_lines)-1
	finish_line_to_print=finish_line_validator(pattern, "\nВведіть кінцевий номер рядка файлу : ", start_line_to_print, number_lines)-1

	print(CRED + "\nВміст файлу з " + str(start_line_to_print) + " до " + str(finish_line_to_print) + " рядку." + CEND)
	for i in range(start_line_to_print, finish_line_to_print+1):
		print(CGREEN + file_lines[i] + CEND)

	file.close()

	file=open("task1.py", 'r', encoding = "utf-8")
	print("\nВесь вміст файлу: ")
	for i in range (0, number_lines):
		s = file.readline()
		print(CCYAN + s + CEND)
	"""file_lines = [line.strip() for line in file]

	for i in range(len(file_lines)):
		print(file_lines[i])"""

	file.close()
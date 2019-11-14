#import sys
from task1 import start1
from task2 import start2
print("\nЛабораторна робота №4 \nПиндиківський Тарас, КМ-93")
print("16 варіант")


while True:
	cont=input("\nНатисніть Enter, щоб продовжити, будь-що інше, щоб завершити роботу з програмою ")
	if(cont!=''): 
		break
	while True:
		try:
			task_number=int(input("\nВведіть номер програми задачі для запуску її виконання (1/2) : "))
			break
		except ValueError:
			print("\nВведіть коректний номер програми!")
			continue
	if(task_number==1):
		start1()
	elif(task_number==2):
		start2()
#	break
#sys.exit()
#D:\Taras Pyndykivskiy\kpi\programming\programming_1\laboratory_works\#4
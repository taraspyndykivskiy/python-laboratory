
import random
def in_range(element, start_point, finish_point):
	if((element>=start_point)and(element<=finish_point)):
		return True
	else:
		return False
def start1():
	initial_list=[]
	while True:
			try:
				list_size=int(input("\nВведіть розмір початкового списку : "))
				break
			except ValueError:
				print("Введіть коректне значення розміру списку")
				continue
#	list_size=random.randrange(100, 1001, 1)
	for i in range (list_size):
		initial_list.append(random.randrange(0, 1001, 1))
	print("\nСписок із елементами :")
	print(initial_list)
	def enter_values():
		while True:
			try:
				start_point=int(input("\nВведіть мінімум діапазону : "))
				finish_point=int(input("\nВведіть максимум діапазону : "))
				break
			except ValueError:
				print("Введіть коректні значення мінімуму та максимуму")
				continue
		return start_point, finish_point
	start_point, finish_point=enter_values()
#	if(((start_point<1)or(start_point>initial_list[list_size-2])or(start_point>finish_point))or((finish_point<1)or(finish_point>list_size-1)or(finish_point<start_point))):
#		enter_values()
	if(start_point>finish_point):
		enter_values()
	appropriate_indexes=[]
	for i in range(len(initial_list)):
		if ((initial_list[i]>=start_point) and (initial_list[i]<=finish_point)):

			appropriate_indexes.append(i)
	appropriate_elements=[initial_list[i] for i in range(len(initial_list)) if in_range(initial_list[i], start_point, finish_point)==True]
	print("\nБуло знайдено " + str(len(appropriate_indexes)) + " елементів, що входять у діапазон : ")
	print(appropriate_elements)
	print("\nЇх індекси : ")
	print(appropriate_indexes)

	while True:
		try:
			number_to_compare=int(input("\nВведіть значення числа для порівняння : "))
			break
		except ValueError:
			print("Введіть коректне значення числа для порівняння")
			continue
	appropriate_elements=[element for element in (initial_list) if element>number_to_compare]	
	appropriate_indexes=[i for i in range(len(initial_list)) if initial_list[i]>number_to_compare]
	print("\nЕлементи, які більші вказаного значення : ")
	print(appropriate_elements)
	print("\nЇх індекси : ")
	print(appropriate_indexes)	

#start1()



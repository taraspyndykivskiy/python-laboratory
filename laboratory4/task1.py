import sys
print("\nЛабораторна робота №4 \nПиндиківський Тарас, КМ-93")
print("16 варіант")
print("Завдання 1: Написати функцію множення дробу на дріб.")
def divisors(number):
	list_index=0
	list_divisors=[None]*100
	divisor_type=2
	number_copy=number
	if(number==1):
		list_divisors.append(1)
	else:
		while(number!=1):
			while(number%divisor_type==0):
				list_divisors.append(divisor_type)
				#list_divisors[list_index]=divisor_type
				number/=divisor_type
		#		list_index+=1
			divisor_type+=1
#	print("\n\n"+str(list_divisors))
	return list_divisors

while True:
	cont=input("\nНатисніть Enter, щоб продовжити, будь-що інше, щоб завершити роботу з програмою ")
	if(cont!=''): 
		break
	print("Для обчислення значення множення дробу (A/B)*(C/D): ")
	while True:
		try:
			number_a=int(input("\nВведіть значення натурального числа А : "))
			number_b=int(input("Введіть значення натурального числа В : "))
			number_c=int(input("Введіть значення натурального числа C : "))
			number_d=int(input("Введіть значення натурального числа D : "))
			if((number_a<=0)or(number_b<=0)or(number_c<=0)or(number_d<=0)):
				print("\n Увага, введіть коректні значення чисел ! \n")
				continue
			break	
		except ValueError:
			continue
	#divisors(number_a)
	numerator=number_a*number_c
	denominator=number_b*number_d
	"""w, h = 2, 10;
	numerator_list = [[0 for x in range(w)] for y in range(h)]
	denominator_list = [[0 for x in range(w)] for y in range(h)]"""
	numerator_list=[None]*100
	denominator_list=[None]*100
	numerator_list=divisors(numerator)
	denominator_list=divisors(denominator)
#	print(str(denominator_list))
	"""for value in range(number_a*number_b):
		for index in range(len(numerator_list[0])):
			if(numerator[0][index]!=0):
				numerato[1][value]==numerator[0][index]	"""
	for i in range(len(numerator_list)):
		for j in range(len(denominator_list)):
			if(numerator_list[i]==denominator_list[j]):
				numerator_list[i]=denominator_list[j]=0
			else :
				continue
	final_numerator=final_denominator=1
	for i in range(len(numerator_list)):
		if(numerator_list[i]!=0):
			final_numerator*=numerator_list[i]
	for i in range(len(denominator_list)):
		if(denominator_list[i]!=0):
			final_denominator*=denominator_list[i]	
	
	print("\nРезультат дії множення : "+str(final_numerator)+ " / "+str(final_denominator))
sys.exit()
#D:\Taras Pyndykivskiy\kpi\programming\programming_1\laboratory_works\#4 (master -> origin)
#λ python multiplication.py

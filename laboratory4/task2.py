import sys
def equal_lenght(word1, word2):
	if(len(word1)!=len(word2)):
		return False
	else:
		return True
while True:
	cont=input("\nНатисніть Enter, щоб продовжити, будь-що інше, щоб завершити роботу з програмою ")
	if(cont!=''): 
		break
	print("\n")
	while True:
		try:
			init_sentence1=str(input("Введіть першу рядкову величину : "))
			init_sentence2=str(input("Введіть другу рядкову величину : "))
			break
		except ValueError:
			continue
	sentence1=init_sentence1.replace(" ", "")
	sentence2=init_sentence2.replace(" ", "")
	result=True
	if(equal_lenght(sentence1, sentence2)==False):
		result=False
	else:
		for i in range (len(sentence1)):
			if(sentence1[i]!=sentence2[i]):
				result=False
				break
	print('\n')
	if(result==True):
		print("Введені рядкові величини рівні.")
	else:
		print("Введені рядкові величини не рівні.")
sys.exit()
#D:\Taras Pyndykivskiy\kpi\programming\programming_1\laboratory_works\#4 (master -> origin)

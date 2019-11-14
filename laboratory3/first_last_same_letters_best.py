import sys
print("\nЛабораторна робота №3 \nПиндиківський Тарас, КМ-93")
print("16 варіант")
print("Завдання : Вивести всі слова, у яких перша і остання літери однакові")
while True:
	cont=input("\nНатисніть Enter, щоб продовжити, будь-що інше, щоб завершити роботу з програмою ")
	if(cont!=''): 
		break
	while True:
		try:
			sentence=str(input("Введіть речення з словами : "))
			break
		except ValueError:
			continue
	words=sentence.split()
	print("\nСлова, які мають однаковий перший і останній символ :")
	for word in words:
		if (word[0]==word[len(word)-1]):
			print(word)
sys.exit()
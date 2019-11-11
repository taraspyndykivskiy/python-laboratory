"""
Створити програму для обчислення тривалості року 
на двох планетах по введених їх радіусах орбіт і
швидкості руху по орбітах. З'ясувати, чи правда, 
що рік на першій планеті довше, ніж на другий. 
"""
import math
import re

re_number = re.compile("^[+-]?[0-9]*\.?[0-9]*$|")

def validator(pattern, prompt):
    text = input(prompt)
    while not bool(pattern.findall(text)[0]):
        text = input(prompt)
    return text

def number_validator(prompt):
    number = float(validator(re_number, prompt))
    while number <= 0:
        number = float(validator(re_number, prompt))
    return number

print("\nЛабораторна робота №1 \nПиндиківський Тарас, КМ-93")
print("16 варіант")
print("Завдання 1: визначення тривалості року на планетах")

radius_first_planet = number_validator('\nВведіть радіус першої планети : ')
speed_first_planet = number_validator("\nВведіть швидкість руху першої планети : ")
radius_second_planet = number_validator("\nВкажіть радіус другої планети : ")
speed_second_planet = number_validator("\nВведіть швидкість руху другої планети : ")

year_duration_first = (2*radius_first_planet *
                       math.pi)/(speed_first_planet)
year_duration_second = (2*radius_second_planet *
                        math.pi)/(speed_second_planet)
print("\n")
if(year_duration_first > year_duration_second):
    print("Тривалість року на першій планеті більша.")
elif(year_duration_first < year_duration_second):
    print("Тривалість року на другій планеті більша.")
else:
    print("Тривалість року на обох планетах однакова.")


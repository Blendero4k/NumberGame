import random
unknownNumber = random.randint(1,10)
number = input("Введите число: ")
if(unknownNumber==number):
    print("Вы угадали!")
else:
    print("Вы не угадали(")
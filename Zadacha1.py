# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.


a = int(input('Введите номер дня недели '))

if 0 < a <= 5:
    print('Это будний день')
elif 5 < a <= 7:
    print('Это выходной день')
else :
    print('Указан не коректный номер дня')
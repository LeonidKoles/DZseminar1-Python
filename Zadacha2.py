# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


xyz = ["X", "Y", "Z"]
ar = []
for i in range(3):
    ar.append(input(f'Введите значение {xyz[i]}: '))

left = not (ar[0] or ar[1] or ar[2])
right = not ar[0] and not ar[1] and not ar[2]
result = left == right

if result == True:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')
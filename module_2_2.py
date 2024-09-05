first = int(input('Введите первое число:'))
second = int(input('Введите второе число:'))
fhird = int(input('Введите третье число:'))

if first == second == fhird:
    print(3)
if first == second or second == fhird or first == fhird:
    print(2)
else:
    print(0)
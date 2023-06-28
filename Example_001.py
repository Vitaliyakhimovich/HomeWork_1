# Найдите сумму цифр трехзначного числа

print("Введите трехзначное число")
num = int(input())
if num > 100 and num < 999:
    a = num % 10
    b = num // 10 % 10
    c = num // 100
    sum = a + b + c
    print(f"Сумма равна ={sum}")
else:
    print("Вы ввели неправильное число")

s = int(input())  # ввод суммы
p = int(input())  # ввод произведени
for x in range(1, 1001):  # перебираем все возможные числа от 1 до 1000 включительно
    y = s - x  # находим второе число по сумме и первому
    if x * y == p:  # если произведение равно данному, то мы нашли числа
      print(x, y)
      break  # прерываем цикл, т.к. мы уже нашли решение

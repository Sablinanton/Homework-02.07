# Homework-02.07
# Создание кортежа из 6 элементов разных типов данных (конечно же, с помощью чатгпт, но я понимаю смысл)))
kortezh = (4, 3.14, 'Kuku', True, None, [1, 2, 3])
# 4 — это целое число (integer).
# 3.14 — это число с плавающей запятой (float).
# 'Kuku' — это строка (string).
# True — это логическое значение (boolean).
# None — это специальное значение, представляющее отсутствие значения (NoneType).
# [1, 2, 3] — это список (list).Kortezh = (4, 3.14, 'Kuku', True, None, [1, 2, 3])
# Вывод на экран типа каждого элемента
# element не требует присвоения, так как переменная element автоматически берет на себя значения из кортежа (как объяснил мне чатгпт)
# цикл for проходит по каждому элементу кортежа, а element поочередно принимает значение текущего элемента кортежа и поочередно выводит после print на экран
for element in kortezh:
    print(type(element))
# сложность алгоритма O(n) - линейная сложность

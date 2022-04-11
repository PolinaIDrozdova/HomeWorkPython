#1
# def numb (n):
#     for i in range(n+1):
#         if i % 2 != 0:
#             yield i
#
# a = numb(5)
#
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

#2
# n = int(input("Введите число: "))
# # первоначальный код был такой: a = (i % 2 != 0 for i in range(n+1)) - он выдавал значения True/False
# a = (i for i in range(n+1) if i % 2 != 0)
# for i in range(n):
#     print(next(a))

#3
# tutors = [
#     'Иван', 'Анастасия', 'Петр', 'Сергей',
#     'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]
#
# gen_names = ((tutor, klass) for tutor, klass in zip(tutors, klasses))
#
# print(next(gen_names))

#4 вывести те элементы, значения которых больше предыдущего
# list_numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# list_num = (num for i, num in enumerate(list_numbers) if num > list_numbers[i-1] and i != 0) #i != 0 исключает 0 элемент
#
# print(next(list_num))
# print(next(list_num))
# print(next(list_num))
# print(next(list_num))

#5
numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

#list_new = []
list_new = (i for i in numbers if numbers.count(i) == 1)

# for i in numbers:
#     if numbers.count(i) == 1:
#         list_new.append(i)
#     else:
#         continue

for i in list_new:
    print(i)
#print(next(list_new))
#print([i for i in numbers if numbers.count(i) == 1]) - вывод списком. Не через print - не итерируемые объекты


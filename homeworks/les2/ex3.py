"""
3 Даны 2 списка и список чисел, написать процедуру и распределить числа по спискам
числа четные должны попасть в список even, числа нечетные должны попасть в список odd
"""

numbers = [44, 22, 54, 87, 345, 912, 654, 18, 33, 76, 11]
even = []
odd = []

even = numbers[:3] + numbers[5:8]
even.append(numbers[9])
odd = numbers[3:5]
odd.append(numbers[-1])
print(even, odd)
from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def calc(your_number):
    """Вычисляет квадратный корень."""
    if your_number <= 0:
        return print('Заданное число должно быть больше 0')
    return print('Мы вычислили квадратный корень из введённого вами числа.'
                 f'Это будет: {sqrt(your_number)}')


print(message)
calc(-25.5)

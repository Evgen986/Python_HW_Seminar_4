# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


def check_correct_input():  # Получение от пользователя степени "К" и проверка на корректность ввода
    degree_k = input('Введите степень K>0: ')
    flag = True
    while flag:
        if not degree_k.isdigit() or int(degree_k) <= 0:
            print('Введено некорректное значение! Введите степень K>0:', end=' ')
            degree_k = input()
        else:
            flag = False
    return int(degree_k)


def polynomial_creation(degree):  # Функция создания многочлена
    coefficient = [randint(1, 100) for monomial in range(1, degree + 2)]
    polynomial = ''
    for index in range(len(coefficient) - 1, -1, -1):
        polynomial += str(coefficient[index]) + 'x^' + str(index) + ' + '
    polynomial = polynomial[:-3].replace('x^0', '').replace('x^1', 'x') + ' = 0'
    return polynomial


def write_to_file(name, text):  # функция записи в файл
    file = open(str(name), 'w')
    file.write(text)
    file.close()


def main():
    coef_1 = check_correct_input()
    poly_1 = polynomial_creation(coef_1)
    print(poly_1)
    write_to_file('polynomial_1.txt', poly_1)

    # Второй многочлен для следующей задачи
    coef_2 = check_correct_input()
    poly_2 = polynomial_creation(coef_2)
    print(poly_2)
    write_to_file('polynomial_2.txt', poly_2)


if __name__ == '__main__':
    main()

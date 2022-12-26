# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

def check_correct_input():  # Получение от пользователя числа N и проверка на корректность ввода
    num = input('Введите число N>1: ')
    while not num.isdigit():
        print('Введено некорректное значение! Введите число N>1:', end=' ')
        num = input()
    return int(num)


def find_prime_factors(n):  # Разложение числа N на простые множители
    if n < 2:
        return [n]
    factors_list = []
    while n > 1:
        for factor in range(2, n+1):
            if n % factor == 0:
                count = 0
                for i in range(2, factor+1):
                    if factor % i == 0:
                        count += 1
                if count == 1:
                    factors_list.append(factor)
                    n //= factor
                    break
    else:
        return factors_list


def main():
    number = check_correct_input()
    print(f'Для числа {number} простыми множителями являются => {find_prime_factors(number)}')


if __name__ == '__main__':
    main()

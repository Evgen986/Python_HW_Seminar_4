# Задача №30: Вычислить число c заданной точностью d. Пример:
# при d = 0.001,π = 3.141             10^(-1)≤d≤10^(-10)

from math import pi


def main():
    while True:
        num = input('Введите число для задания точности числу ПИ в формате "0.000" или укажите разрядность: ')
        if '.' in num or ',' in num:
            num = num.replace(',', '.')
            index = (len(num)-1) - num.index('.')
            break
        elif num.isdigit():
            index = int(num)
            break
        else:
            print('Введено некорректное значение! Попробуйте еще раз')
    print(f'При точности {index} число ПИ = {(round(pi, index))}')


if __name__ == '__main__':
    main()
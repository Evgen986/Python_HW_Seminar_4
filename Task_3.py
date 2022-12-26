# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def get_digital_list():  # Получение послед. чисел от пользователя, проверка и удаление всего, что не относится к цифрам
    nums = input('Введите последовательность чисел через пробел: ').split()
    for index in range(len(nums)-1, -1, -1):
        if not nums[index].isdigit():
            nums.pop(index)
    return nums


def remove_duplicates(str_list):  # Удаление повторяющихся значений в получаемом листе
    str_list.sort()
    index_start = len(str_list)-1
    while index_start > 0:
        count = 0
        for index_finish in range(index_start-1, -1, -1):
            if str_list[index_finish] == str_list[index_start]:
                count += 1
            else:
                break
        if count > 0:
            for count_del in range(count+1):
                str_list.pop(index_start-count_del)
        index_start = index_finish
    return str_list


def main():
    my_list = get_digital_list()
    print(f'{my_list} => {remove_duplicates(my_list)}')


if __name__ == '__main__':
    main()

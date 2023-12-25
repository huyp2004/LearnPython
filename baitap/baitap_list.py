import math


# Bài tập 1: Tìm số lớn nhất trong một danh sách. 12, 45, 89, 7, 23, 56, 91, 2 --> 91
def bt1():
    my_list = [12, 45, 89, 7, 23, 56, 91, 2]

    max = float('-inf')  # Am vo cuc
    for i in my_list:
        if max < i:
            max = i
    return max


# Bài tập 2: Tính tổng các số chẵn trong danh sách. 10, 25, 8, 14, 27, 46, 33, 20 --> 98
def bt2():
    my_list = [10, 25, 8, 14, 27, 46, 33, 20]
    result = 0
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            result += my_list[i]

    # List comprehension
    # total = sum(0))
    return result

# Bài tập 3: Loại bỏ các phần tử trùng lặp từ danh sách
# VD: 1, 2, 3, 4, 2, 5, 6, 1, 7, 8, 9, 3 --> 1, 2, 3, 4, 5, 6, 7, 8, 9


def bt3():
    my_list = [1, 2, 3, 4, 2, 5, 6, 1, 7, 8, 9, 3]
    resullt = []

    for i in range(len(my_list)):
        if my_list[i] not in resullt:
            resullt.append(my_list[i])
    return resullt


# Đảo ngược danh sách. vd: 11, 22, 33, 44, 55 -> 55, 44, 33, 22, 11
def bt4():
    my_list = [11, 22, 33, 44, 55]
    my_list.reverse()
    # cách đảo ngược đơn giản
    #result = my_list[::-1]
    return my_list


# Tìm các số nguyên tố trong danh sách. 17, 8, 23, 45, 11, 32, 19, 13 --> 17, 23, 11, 19, 13
def bt5():
    my_list = [17, 8, 23, 45, 11, 32, 19, 13]
    prime_list = []

    for i in range(len(my_list)):
        prime = True

        for j in range(2, int(math.sqrt(my_list[i])) + 1):
            if my_list[i] % j == 0:
                prime = False
                break
        if prime:
            prime_list.append(my_list[i])
        else:
            continue

    return prime_list

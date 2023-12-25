import time
import threading

# VD: có nhiều luồng từ 5 đến 6 luồng trở lên


def buble_sort(lst_number):
    for i in range(len(lst_number)):
        for j in range(i+1, len(lst_number)):
            if lst_number[i] > lst_number[j]:
                lst_number[i], lst_number[j] = lst_number[j], lst_number[i]
                time.sleep(0.075)
    print(lst_number)


if __name__ == '__main__':
    lst = [[9, 6, 8, 4, 55, 66, 7, 1], [20, 56, 61, 14, 30, 88, 12, 67, 52, 48],
           [60, 50, 14, 69, 59, 25], [67, 77, 81, 57, 94, 74],
           [52, 50, 50, 84, 22, 2], [40, 75, 83, 74, 5, 13]]

    # start = time.time()
    # for i in lst:
    #     my_thread = threading.Thread(target=buble_sort, args=(i,))
    #     my_thread.start()
    # end = time.time()
    # print(round(end- start, 5))

    # print("no multi")

    start_step2 = time.time()
    for i in lst:
        buble_sort(i)
    end_step2 = time.time()
    print(round(end_step2 - start_step2, 5),)
'''
Bài tập 1: Tính tổng các số từ 1 đến n --> sum_to_n(5)  # Kết quả: 15
Bài tập 2: Tính giai thừa --> factorial(5)  # Kết quả: 120
Bài tập 3: Tìm ước chung lớn nhất (UCLN) --> gcd(24, 36)  # Kết quả: 12
- Sử dụng thuật toán euclid tìm ước chung lớn nhất: ucln(a, b) = ucln (b, số lớn nhất (a,b) - (số nhỏ nhất a,b)).
 đến khi a == b thì ra ước chung lớn nhất
Bài tập 4: In dãy Fibonacci --> dãy fibonacy từ 1 tới 10 # Kết quả: 0 1 1 2 3 5 8 13 21 34
'''


def sum_to_n(num):
    if num == 1:
        return 1
    else:
        return num + sum_to_n(num - 1)


def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


def ucln(a, b):
    if a == 0 or b == 0:
        return a + b
    else:
        return ucln(b, max(a, b)-min(a, b))

# max_ab = 0 # một cách khác ko cần sử dụng eclid
# for i in range(1, 26 % 38):
#     if 26 % i == 0 and 38 % i == 0:
#         print('ước chung của 26 và 38:', i)
#         max_ab = i

def fibonacy(num):
    if num <= 1:
        return num
    else:
        return fibonacy(num - 1) + fibonacy(num - 2)


if __name__ == '__main__':
    print('De quy tong: 1 + 2 + 3 + ... + n =', sum_to_n(5))
    print('Giai thua cua 5:', factorial(5))
    print('Ước chung lớn nhất:', ucln(24, 36))
    for i in range(10):
        print(fibonacy(i), end=" ")
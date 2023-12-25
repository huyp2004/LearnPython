'''
De quy (recursion)
Đệ quy là một hàm tự gọi lại chính nó

def dequy(n):
    Phần cơ sở: nếu n thỏa mãn điều kiện dừng, trả về giá trị cụ thể
    if n == ...:
        return ...
    Phần đệ quy: nếu n không thỏa mãn điều kiện dừng, trả về kết quả của hàm dequy với đối số khác
    else:
        return dequy(...)

    Tìm 28tech rồi xem video 'Bài 16. Hàm Đệ Quy Trong Python' để hiểu rõ hơn
'''


def s(num):
    if num == 1:
        return 1
    else:
        return num + s(num - 1)

if __name__ == '__main__':
    n = 4
    print(s(n))
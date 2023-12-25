'''
1. Sắp Xếp Danh Sách: Viết một hàm có tên là sap_xep_danh_sach nhận vào một danh sách số nguyên 
và trả về danh sách đã được sắp xếp theo thứ tự tăng dần.

2. Chuyển Đổi Số Lẻ và Chẵn: Viết một hàm có tên là chuyen_doi_le_chan nhận vào một danh sách số nguyên
 và trả về hai danh sách con, một chứa các số lẻ và một chứa các số chẵn.

3. Xác Định Chuỗi Palindrome: Viết một hàm có tên là palindrome nhận vào một chuỗi và trả về True nếu chuỗi đó là chuỗi palindrome,
 False nếu không phải.

4. Tìm Các Số Hoàn Hảo: Viết một hàm có tên là tim_so_hoan_hao nhận vào một số nguyên dương và trả về True nếu số đó là số hoàn hảo,
 False nếu không phải. Một số hoàn hảo là số có tổng các ước số bằng chính nó.

5. Đổi Đầu vào Ngày Tháng Năm: Viết một hàm có tên là doi_ngay_thang_nam nhận vào một chuỗi đại diện cho ngày tháng năm dưới dạng "dd/mm/yyyy" 
và trả về một chuỗi mới với định dạng "tháng ngày, năm".

6. Tính Số Fibonacci: Viết một hàm có tên là tinh_so_fibonacci nhận vào một số nguyên dương n và trả về số Fibonacci thứ n.
'''


def sap_xep_danh_sach(num_list):
    number_sorted = sorted(num_list)
    return number_sorted


def chuyen_doi_le_chan(num_list):
    odd_number = []
    even_number = []
    for num in num_list:
        if num % 2 == 0:
            even_number.append(num)
        else:
            odd_number.append(num)
    return odd_number, even_number


def palindrome(num):
    so_goc = num
    so_tra_ve = 0
    while num > 0:
        a = num % 10
        so_tra_ve = so_tra_ve * 10 + a
        num //= 10

    return so_goc == so_tra_ve


def doi_ngay_thang_nam(ngay, thang, nam):
    return f'{thang} {ngay}, {nam}'

def fibonacci(n):
    if n <= 0:
        return 'n phai > 0'
    a = [0, 1]
    for i in range(2, n):
        a.append(a[-1] + a[-2])
    return a

print(fibonacci(10))
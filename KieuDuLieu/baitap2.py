# viet chuong trinh tinh tong 2 so nguyen a, b. Xu ly ngoai le khi nguoi dung nhap sai kieu du lieu

try:
    a = int(input("Nhap vao so nguyen a: "))
    b = int(input("Nhap vao so nguyen b: "))
    total = a + b
    print("Tong cua 2 so nguyen a + b =", total)
except ValueError:
    print("Ban da nhap dinh dang dau vao khong hop le!")

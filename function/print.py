# Hàm main dùng để quản lý các function và chứa, gọi function 
def main():
    hs_a = "Phan Nguyễn Quốc Huy"
    nam_sinh_a = 2004
    hs_b = "Bùi Thanh Nga"
    nam_sinh_b = 2003

    student_a(hs_a, nam_sinh_a)
    student_b(hs_b, nam_sinh_b)


# In ra màn hình tên của học sinh A
def student_a(name, age):
    print('Tên của học sinh là:', name)
    print(f'Tuổi của {name} là {2023 - age} tuổi')
    print()


# in ra màn hình tên của học sinh A
def student_b(name, age):
    print('Tên của học sinh là:', name)
    print(f'Tuổi của {name} là {2023 - age} tuổi')
    print()


main()
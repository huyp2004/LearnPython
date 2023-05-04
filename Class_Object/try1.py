'''
Đây là chương trình quản lý học sinh, sinh viên. gồm chức năng xem, xóa, thêm sinh viên.
Còn một số vẫn chưa được hoàn thiện:
    1. MSSV không được trùng nhau. Nếu ta chọn mssv để xóa thì sẽ dễ xóa nhầm người có trùng MSSV
    2. Function Xóa sinh viên chỉ được xóa 1 sinh viên
    
'''

from student import *

list_student = []

def add_student():
    try:
        # Nhập thông tin
        full_name = input("Nhap ho ten> ").title()
        mssv = input("Nhap MSSV> ")
        old = int(input("Nam sinh> "))

        # chọn đối tượng Class
        info = Student(full_name, mssv, old)

        list_student.append(info)
        print("Đã thêm sinh viên", info.name)
    except:
        print('Bạn nhập sai năm sinh. Hãy nhập lại')

# Xem sinh viên
def show_student():
    if len(list_student) == 0:
        print("Không có sinh viên nào")
    else:
        for i in list_student:
            i.show()
            print("---------------")

# Xóa sinh viên bằng MSSV
def remove_student():
    check_mssv = input("Nhập MSSV để xóa> ") 

    # Check có hoặc không
    found = False

    for i in list_student:
        if check_mssv == i.get_id():  
            list_student.remove(i)
            print("Đã xóa sinh viên có MSSV:", check_mssv )
            found = True

    # Trường hợp không có
    if not found:
        print('Không có MSSV này')


def main():
    while True:
        choose = int(input('''
        Chọn chức năng:
        1. Xem sinh viên
        2. Thêm sinh viên
        3. Xóa sinh viên
        4. Thoát
        > '''))

        try:
            if isinstance(choose, int):
                if choose == 1: # Xem
                    show_student()
                elif choose == 2: # Thêm
                    add_student()
                elif choose == 3: # Xóa
                    remove_student()
                elif choose == 4: # Thoát
                    break
                else:
                    print("Bạn chọn sai chức năng")
            else:
                print("Bạn hãy nhập số để sử dụng chức năng")
        except:
            print("Vui lòng nhập số để chọn chức năng")


if __name__ == "__main__":
    main()
from os import name
from Class_Student import Student


def show_student(student_list):
    if len(student_list) == 0:
        print('\nThông báo! Hiện chưa có sinh viên nào\n')
    else:
        for i in student_list.values():
            i.show()


def add_student(student):
    id = input('Nhập MSSV sinh viên: ')
    if id.isdigit():
        name = input('Nhập tên sinh viên: ').title()
        class_study = input('Nhập lớp sinh viên: ').upper()
        student[id] = Student(id, name, class_study)
        print('\nSinh viên đã được thêm vào!\n')
        return student
    else:
        print('\nBạn nhập sai định dạng mssv!\n')


def delete_student(mssv, student_list):
    if student_list[mssv].id in student_list:
        student_list.pop(mssv)

        print(f'\nSinh viên có MSSV {mssv} đã được xóa\n')
    else:
        print('\nKhông có sinh viên này trong danh sách\n')

    return student_list


def change_student(mssv, student_list):
    if mssv in student_list:
        change = input('''
    0. Họ và tên
    1. Lớp
    Nhập lựa chọn sửa: ''')
        if change == '0':
            name = input("Nhập họ và tên sửa: ").title()
            student_list[mssv].set_name(name)

        elif change == '1':
            lop = input("Nhập lớp sửa: ").upper()
            student_list[mssv].set_class_study(lop)
        else:
            print('\nBạn nhập sai lựa chọn\n')
    else:
        print('\nKhông tồn tại mssv này\n')
    return student_list


def menu_setting(student_list):
    print('''Chọn chức năng muốn sử dụng:
        0. Thoát
        1. Xem danh sách sinh viên
        2. Thêm sinh viên
        3. Xóa sinh viên
        4. Sửa sinh viên''')
    choice = input('Bạn sử dụng chức năng: ')

    if choice == '0':
        exit()

    elif choice == '1':
        show_student(student_list)

    elif choice == '2':
        add_student(student_list)

    elif choice == '3':
        mssv = input('Vui lòng nhập MSSV để xóa: ')
        delete_student(mssv, student_list)

    elif choice == '4':
        show_student(student_list)
        mssv = input('Nhập MSSV muốn sửa: ')

        change_student(mssv, student_list)
    else:
        print('Bạn chọn sai chức năng, vui lòng chọn lại.')


if __name__ == '__main__':
    student = {}
    while True:
        menu_setting(student)


print('AS*D^AJZ>A')
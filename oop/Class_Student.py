# class trong python
'''
Gom các đối tượng lại vào trong một class. Đối tượng SinhVien
Có 2 phương thức: get, set
- get: lấy đối tượng
- set: thiet lap doi tuong
'''


class Student:
    count_student = 0

    def __init__(self, id, name, class_study):  # Thuộc tính
        self.id = id
        self.name = name
        self.class_study = class_study

        Student.count_student += 1

    def set_name(self, name):  # ID khong the thay doi nen ta set name
        self.name = name

    def set_class_study(self, class_study):
        self.class_study = class_study

    def get_class_study(self):
        return self.class_study

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def show(self):
        print(f'\nMSSV: {self.id}')
        print(f'Họ và tên: {self.name}')
        print(f'Lớp: {self.class_study}')

'''
Phương thức getter cần đánh dấu với @property decorator.
Phương thức setter cần đánh dấu với cấu trúc @tên_property.setter, 
phương thức deleter cần đánh dấu với cấu trúc @tên_property.deleter. 
Ví dụ, với age property thì setter phải đánh dấu @age.setter, deleter phải đánh dấu @age.deleter.
'''


class Nguoi:
    def __init__(self, fname, lname, scores: int):
        self.__fname = fname
        self.__lname = lname
        self.__scores = scores

    @property
    def first_name(self):
        return self.__fname

    @first_name.setter
    def first_name(self, fname):
        self.__fname = fname

    @property
    def last_name(self):
        return self.__lname

    @last_name.setter
    def last_name(self, lname):
        self.__lname = lname

    @property
    def full_name(self):
        return f"{self.__lname} {self.__fname}"

    @property
    def score(self):
        return self.__scores

    @score.setter
    def score(self, scores):
        self.__scores = scores


person = Nguoi('Huy', 'Phan Nguyen Quoc', 94)
print("Ho va ten:", person.full_name)
print("Diem tong ket:", person.score)
person.first_name = 'Anh'
person.last_name = 'Nguyen Ngoc'
print("Ho va ten:", person.full_name)
'''
Tạo một lớp Hình chữ nhật với các thuộc tính chiều dài và chiều rộng bị ẩn.
Viết các phương thức getter và setter cho các thuộc tính này.
Viết một phương thức tính diện tích của hình chữ nhật.
'''


class HinhChuNhat:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def set_length(self, length):
        self.length = length

    def get_length(self):
        return self.length

    def set_width(self, width):
        self.width = width

    def get_width(self):
        return self.width

    def tinh_dien_tich(self):
        return self.length * self.width


dien_tich_hcn = HinhChuNhat(4, 6)
print(dien_tich_hcn.tinh_dien_tich())
'''
Tạo một lớp Người với các thuộc tính tên, tuổi và giới tính bị ẩn. 
Viết một phương thức str để in ra thông tin của một đối tượng Người. 
Viết một phương thức repr để trả về một chuỗi biểu diễn một đối tượng Người.
'''


class Nguoi:
    def __init__(self, name, old, sex):
        self.__name = name  # isalpha() hàm trả về true nếu có chữ cái
        self.__old = old
        self.__sex = sex

    def infomation(self):
        return f"Ten: {self.__name}\nTuoi: {self.__old}\nGioi tinh: {self.__sex}"

    def __repr__(self):
        return f"Nguoi({self.__name}, {self.__old}, {self.__sex})"


class SinhVien(Nguoi):  # Kế thừa class
    def __init__(self, name, old, sex, scores):
        super().__init__(name, old, sex)  # Kế thừa method
        self.__scores = scores

    # Kiểm tra đậu và rớt
    def __str__(self):
        if self.__scores >= 5:
            return "Ban co the tot nghiep"
        else:
            return "Ban khong the tot nghiep"


a = SinhVien('Huy', 20, 'Nam', 95)
print(a.infomation())

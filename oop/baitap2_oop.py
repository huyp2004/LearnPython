# Cho sanh sách điểm của sinh viên. Viết một lớp SinhVien lấy tham số từ mssv, tên, điểm và sắp xếp theo giảm dần
class SinhVien:
    def __init__(self, id, name, mean_grade: int):
        self.id = id
        self.name = name
        self.mean_grade = mean_grade

    def __str__(self):
        return f"Mã số: {self.id}\nHọ và tên: {self.name}\nĐiểm trung bình: {self.mean_grade}"


sv = [SinhVien('01', 'A', 90), SinhVien('02', 'A', 97), SinhVien('03', 'C', 91)]

sv_sorted = sorted(sv, key=lambda x: x.mean_grade, reverse=True)

for i in sv_sorted:
    print(i)

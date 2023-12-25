class SinhVien:
    def __init__(self, id, name, scores):
        self.__id = id
        self.__name = name
        self.__scores = scores

    def calculate_mean_grade(self):
        mean = 0
        for sv in self.__scores.values():
            mean += sv

        return mean / len(self.__scores)

    
students = {
    '01': SinhVien('01', 'A', {'Toán': 90, 'Lý': 85, 'Hóa': 92}),
    '02': SinhVien('02', 'B', {'Toán': 80, 'Lý': 75, 'Hóa': 70}),
    '03': SinhVien('03', 'C', {'Toán': 95, 'Lý': 90, 'Hóa': 100})
}


for sv in students.keys():
    print(
        f"Sinh viên {sv} có điểm trung bình là {students[sv].calculate_mean_grade()}")

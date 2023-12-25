'''
Bài 1: Tổ chức dữ liệu
Bạn có một danh sách các sinh viên, mỗi sinh viên được biểu diễn bằng một từ điển với các thuộc tính như sau:
{Tên sinh viên: Alice, Tổi: 20, Điểm số: 90,
.....
 Thêm các sinh viên khác vào
}
Viết một hàm tên là sort_students sắp xếp Sinh viên theo số điểm giảm dần

Bài 2: Thống kê dữ liệu
Bạn có một danh sách các số nguyên. Hãy viết một hàm có tên là analyze_numbers nhận danh sách này và trả về một từ điển chứa thông tin sau:

Tổng của các điểm.
Số lượng các điểm.
Trung bình cộng của các điểm.
Số điểm lớn nhất và số điểm nhỏ nhất
'''

students = [
    {'name': 'Alice', 'age': 20, 'grades': 90},
    {'name': 'Bob', 'age': 25, 'grades': 100},
    {'name': 'Jhon', 'age': 23, 'grades': 89},
    {'name': 'Phan Nguyen Quoc Huy', 'age': 20, 'grades': 100},
    {'name': 'Nguyen Ngoc Anh', 'age': 20, 'grades': 87},
    {'name': 'Do Huy Hoang', 'age': 20, 'grades': 63}
]


def add_students():
    try:
        name = input("Nhập tên sinh viên: ")
        age = int(input("Nhập tuổi sinh viên: "))
        grades = int(input("Nhập điểm sinh viên: "))
        if grades < 0 or grades > 100:
            print("Bạn nhập sai điểm. Điểm số giới hạn từ 0 đến 100")
            grades = int(input("Nhập lại điểm sinh viên: "))

        students.append({'name': name, 'age': age, 'grades': grades})

        return students

    except ValueError:
        print("Bạn nhập sai kiểu đinh dạng rồi, vui lòng nhập lại nhé")
        name = input("Nhập tên sinh viên: ")
        age = int(input("Nhập tuổi sinh viên: "))
        grades = int(input("Nhập điểm sinh viên: "))

    return students


def sort_students(student):
    # for i in range(len(student)):
    #     for j in range(i+1, len(student)):
    #         if student[i]['grades'] < student[j]['grades']:
    #             student[i], student[j] = student[j], student[i]S

    return sorted(student, key=lambda num: num['grades'], reverse=True)


def analyze_numbers(grades):

    analyze = {
        'sum': sum(grades),
        'count': len(grades),
        'average': round(sum(grades) / len(grades), 2),
        'max': max(grades),
        'min': min(grades)
    }

    return analyze


# Run function (not run add_students)
student_sorted = sort_students(students)
for i in range(len(student_sorted)):
    print(f'- STT {i+1}:', end=' ')
    print(f"{student_sorted[i]['name']} - {student_sorted[i]['grades']}")


grades_use_analyze = [student['grades'] for student in student_sorted]
analyze = analyze_numbers(grades_use_analyze)
print(analyze)

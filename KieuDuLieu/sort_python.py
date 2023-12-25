# Một số thủ thuật xắp xếp

students = [
    {'name': 'Alice', 'age': 20, 'grades': 90},
    {'name': 'Bob', 'age': 25, 'grades': 100},
    {'name': 'Charlie', 'age': 23, 'grades': 89},
]

number_sorted = sorted(students, key=lambda x: x['grades'], reverse=True)
print(number_sorted)

a = lambda x: students[0]['grades'] + students[1]['grades']
print(a)
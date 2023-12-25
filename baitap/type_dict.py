# Dict kieu du lieu duoc dinh dang bang {key: value}

my_dict = {
    'name': 'Phan Nguyen Quoc Huy',
    'age': 20,
    'Address': "An Phu, Thuan An, Binh Duong"
}

print(my_dict)

my_dict['age'] += 1
my_dict['Skill'] = 'Python, Linux Ubuntu'
print(my_dict)

# Duyet dict
for key, value in my_dict.items():
    print(key, value)

print('--'*10)
# Duyet key cua dict
for key in my_dict.keys():
    print(key)

print('--'*10)
# Duyet value cuar dict
for value in my_dict.values():
    print(value)

numb = {
    'a': float('-inf'),
    'min': 0
}
lst = [1, 2, 3, 4, 5]

for i in lst:

    numb['a'] += i

print(numb)
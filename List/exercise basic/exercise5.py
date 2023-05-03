'''
Viết một hàm nhận đầu vào là hai list
 và trả về một list mới chứa các phần tử chung của hai list ban đầu
'''
lst_1 = [7, 8, 9, 10]
lst_2 = [9, 22, 10, 11]

# cach 1
new_list = [i for i in lst_1 if i in lst_2]
print(new_list)

print('--'*10)

# cach 2
better_list = set(lst_1) & set(lst_2)
print(list(better_list))

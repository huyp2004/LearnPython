'''
Viết một hàm nhận đầu vào là một list và trả về một list
mới chỉ chứa các phần tử không trùng lặp trong list ban đầu
'''
# my_list = list(map(int, input("Enter n to list> ").split(" ")))
my_list = [5, 4, 1, 6, 1, 1]
new_list = []
for i in my_list:
    if i not in new_list:
        new_list.append(i)
    else:
        continue
print(new_list)

# Better way two, use set

better_list = list(set(my_list))
print(better_list)
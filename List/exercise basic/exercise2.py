'''
Viết một hàm nhận đầu vào là một list và trả về một list mới
 chỉ chứa các phần tử xuất hiện trong list ban đầu một lần.
'''
# Cách 1
my_list = [1, 2, 2, 3, 4, 4, 4, 5]
dem = {}
for i in my_list:
    if i in dem:
        dem[i] += 1
    else:
        dem[i] = 1
better = [i for i, a in dem.items() if a == 1]
print(better)

# cách 2
better_list = [i for i in my_list if my_list.count(i) == 1]
print(better_list)


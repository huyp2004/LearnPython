'''
Viết một hàm nhận đầu vào là một list và một số nguyên k, trả về một list mới
 chứa các phần tử của list ban đầu được sắp xếp theo thứ tự tăng dần
  và giới hạn độ dài của list mới là k.
'''
my_list = [2, 5, 3, 2, 5, 89]

k = 3

better_list = my_list[:k]

print(better_list)
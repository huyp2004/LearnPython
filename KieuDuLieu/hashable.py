# một biến được lưu bằng một id cụ thể trong bộ nhớ máy tính
# biến số nguyên không thay đổi trong vùng nhớ
# còn lại sẽ thay đổi vùng nhớ

#  phuong thuc += khong thay doi id trong bo nho

a = 10
b = a
print(id(a))
print(id(b))

a2 = id(10);

print("a2 = 10:", a2)
print("id = 10:", id(10))

print("id Huy: ", id('Huy'))
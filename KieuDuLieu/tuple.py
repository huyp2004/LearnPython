# Kieu du lieu tuple
# tupe ít chiếm bộ nhớ hơn list, và nhanh hơn list. sử dụng bằng ()
# Không thể thay đổi dữ liệu bên trong tuple

tup = (1, 2, 2, 5, 3, 4, 6)
print(type(tup))

for i in tup:
    print(i)

a = tup.count(2)
b = tup.index(5) # vị trí của số 5 trong tuple ở index mấy
print("Có mấy con số 2:", a)
print("Hang index của tuple, vị trí:", b)

tong = sum((i for i in tup))

print("Tong cua tuple:", tong)
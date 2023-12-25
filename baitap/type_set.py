# Kieu du lieu set. VD:  my_set = {1, 2, 3}
# Set khong luu du lieu trung lap

my_lst = [1, 1, 2, 3, 5, 1, 51, 647, 347, 221, 3]
my_set = set(my_lst)
print(my_set)

my_set2 = {5, 4, 2, 3, (1, 2, 33)}

print((4 and 5) in my_set2)

a = [1,2,3]
b = [3,4,5]

print(set(a) ^ set(b))
set(a).clear()
print(set(a))


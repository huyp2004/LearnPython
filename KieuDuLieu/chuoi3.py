# cat chuoi
a = "Phan Nguyen Quoc Huy"
b = a.split(" ")

two_split = a.split(" ", 2) # chi cat chuoi khoang trang 2 lan, tu trai qua phai
right_split = a.rsplit(" ", 2) # chi cat chuoi khoang trang 2 lan, tu phai qua trai
char_split = a.split("a") # chi cat chuoi ky tu a

# print(b)
# print(two_split)
# print(right_split)
# print(char_split)
print(a[0:10:1])
# Nhap vao 2 so nguyen a, b. Va tinh tong 2 so do
# a = int(input("Nhap vao so nguyen a: "))
# b = int(input("Nhap vao so nguyen b: "))

# print("Tong cua 2 so nguyen a + b =", a + b)

# c = 121
# print(str(c)[::-1] == c)

nums = [1,5,-2,-4,0]
nums.sort()

number_set = set(nums)

print(len(number_set), '||', len(nums))
print(len(number_set) != len(nums))
# Co ban ve String
print(r'Hello \r World') # bo qua ky tu \n va \r...

a = "Hello World"
b = "My name is Huy"

print(rf'{a} "\n" {b}') # Noi chuoi

print(a * 10) # In ra 10 lan chuoi a

c = a * 10

print(a in c) # Kiem tra chuoi a co trong chuoi c hay khong
print(b[-1]) # Lay ky tu cuoi cung cua chuoi b


for i in range(0, len(a)):
    print(a[i])

print("ky tu thu 3 cua b la:", b[3])

d = a[1:4] # Lay chuoi con tu vi tri 1 den 4 cua chuoi a
print("vi tri 1 den 4 cua chuoi a la:", d)
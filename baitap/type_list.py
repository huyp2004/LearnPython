a = [1, 2, 3, "Huy"]
b = [[1, 2,3], [4, 5, 6], [7, 8, 9]]

# print(b[1][1]) # Lay phan tu thu 2 cua phan tu thu 2 cua b

# Duyet list
for i in range(len(a)):
    print(a[i], end=' ')

# Duyet list truc tiep
for i in a:
    print(i, end=' ')

print("\nDuyet mang 2 chieu")
for i in range(len(b)):
    for j in range(len(b[i])):
        print(b[i][j], end=' ')
    print()

print("\nDuyet mang 2 chieu truc tiep")
for i in b:
    for j in i:
        print(j, end=' ')
    print()

# Them phan tu vao list
c = []
# Them 5 phan tu vao list c
for i in range(5):
    c.append(i)
print(c)

# Rut gon list bang list comprehension
#list_compre = [int(input(f"Nhap phan tu {i+1}: ")) for i in range(5)]

list_compre = [6, 1, 4, 2, 3]
print(list_compre)
# Sap xep list_compre bang bubble sort
# for i in range(len(list_compre)-1):
#     if list_compre[i] > list_compre[i+1]:
#         list_compre[i], list_compre[i+1] = list_compre[i+1], list_compre[i] 
        
print(list_compre)
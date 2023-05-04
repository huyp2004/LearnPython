my_list  = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

lst_3d = [
    [0, 0, 0],
    [0, 0, 1], 
    [0, 1, 0], 
    [1, 0, 0], 
    [1, 1, 1]]

# print(my_list[0][2])

my_list[2][1] = 88

for i in my_list:
    for j in i:
        print(j, end=" ")
    print()
x, y, z, n = 1, 1, 2, 3

coordinates = []

for i in range(x + 1):
    print(f'Vòng lặp i = {i};', end=" ")
    for j in range(y + 1):
        print(f'Vòng lặp j = {j};', end=" ")
        for k in range(z + 1):
            print(f'Vòng lặp k = {k};', end=" ")
            if i + j + k != n:
                coordinates.append([i, j, k])
print()
print(coordinates)
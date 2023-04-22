
# n = int(input())
# a = [int(input()) for i in range(n)]
a = [1, 3, 5, -3]
for i in range(len(a)):
    a[i] *= a[i]

print(a)
def recursion(nums):
    if nums == 1:
        return 1
    else:
        return (nums + recursion(nums-1))


def tong(nums):
    return 1 if nums == 1 else nums + tong(nums - 1)

# 1 Bảng cửu chương
def nhan(nums, i=1):
    if i <= 10:
        print(f'{nums}*{i} = {nums * i}')
        return nhan(nums, i+1)

# Khởi tạo bảng cửu chương từ 2 đến 9
for i in range(2, 10):
    nhan(i)
    print()

# Sắp xếp bằng đệ quy
def buble_sort(arr, n):
    if n == 1:
        return 1
    else:
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i] , arr[i + 1] = arr[i + 1], arr[i]
        buble_sort(arr, n-1)
        return arr

arr = [9,9,7,5,3,5,7,]

arr = buble_sort(arr, len(arr))
print(arr)
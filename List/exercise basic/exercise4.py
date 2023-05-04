'''
Viết một hàm nhận đầu vào là một list và trả về một list mới
chứa các phần tử của list ban đầu được sắp xếp theo thứ tự từ lớn đến nhỏ.
'''

# Cách 1
def sort_list():
    new = sorted(my_list, reverse= True)
    return new
try:
    my_list = list(map(int , input("Enter number > ").split(" ")))
    print(sort_list())
except ValueError:
    print("List Error")

# Cách 2 :Đệ quy buble sort
def sort_recursion(my_list, num):
    if num == 1:
        return 1
    else:
        for i in range(num - 1):
            if my_list[i] <  my_list[i+1]:
                my_list[i+1], my_list[i] = my_list[i], my_list[i+1]
            sort_recursion(my_list, num- 1)
        return my_list

arr = sort_recursion(my_list, len(my_list))
print(arr)
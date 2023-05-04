'''
Viết một hàm nhận đầu vào là một list và một số nguyên k,
 trả về một list mới chứa các phần tử lớn hơn k trong list ban đầu.
'''

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

try:
    k = int(input("Enter number > "))
except:
    k = int(input("Oops wrong number, Enter number > "))

def result_list_greate(lst, num):   
    if not isinstance(lst, list) or not isinstance(num, int):
        return "Oops List from you error, or number from you error"
    else:
        return [i for i in lst if i > num]
    
print(result_list_greate(my_list, k))
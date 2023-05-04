# Input n to list
n = 10

my_list = []
for i in range(n):
    my_list.append(i)

print(my_list)

# Sum list
total_list = sum(my_list)
print(total_list)

# find max and on list
list_max = max(my_list)
print('max list:', list_max)

list_min = min(my_list)
print('min list:', list_min)

# Find second max list
my_list.remove(list_max)
print('second max list:',max(my_list))

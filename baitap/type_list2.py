def my_list():
    mylst = [1, 7, 2, 1, 51, 5]

    # Dem cac phan tu trong list
    c = mylst.count(1)
    print(c)

    count = 0
    for i in mylst:
        if i == 1:
            count += 1
    print(count)

    # Tim vi tri cua phan tu trong list
    d = mylst.index(2)
    print(f'vi tri cua 2 trong list la: {d}')

    for i in range(len(mylst)):
        if mylst[i] == 1:
            print(i)

# Gop 2 list
mylist1 = [1, 2, 3]
mylist2 = [4, 5, 6, 7]

for i in range(len(mylist1)):
    for j in range(len(mylist1)):
        if mylist1[i] not in mylist2:
            mylist2.append(mylist1[i])

print(mylist2)

for i in range(len(mylist2)):
    for j in range(i+1, len(mylist2)):
        if mylist2[i] > mylist2[j]:
            mylist2[i], mylist2[j] = mylist2[j], mylist2[i]
            print(f"After swapping: {mylist2}")
print("sorted list: ", mylist2)
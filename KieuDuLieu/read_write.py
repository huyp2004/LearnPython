# Bài học ghi và đọc file
# read = đọc tất cả các dòng
# readline chỉ đọc một dòng, nếu file chỉ 1 một dòng thì đọc hết
# readlines(): tóm tất cả lại một dòng. ghi chú xuống dòng bằng \n

file = open('./read_write/hello.txt', mode='r', encoding='utf-8')
data_file = file.read()
print(data_file)
file.close()

file = open('./read_write/hello.txt', mode='r', encoding='utf-8')
data_file2 = file.read(5)
print(data_file2)
file.close()

file = open('./read_write/hello.txt', mode='r+', encoding='utf-8')
data_file3 = file.readlines()
print(data_file3)
file.close()

file = open('./read_write/hello.txt', mode='a+', encoding='utf-8')
file.write(' Xin chào, và Huy đã ở đây !')
file.close()

file = open('./read_write/hello.txt', mode='r', encoding='utf-8')
print(file.read())
file.close()

with open("./read_write/hello2.txt", "w+") as file:
    file.write("Hello, this is an example.")
    
    # Di chuyển con trỏ về đầu tập tin để đọc nội dung
    file.seek(0)
    
    # Đọc nội dung từ tập tin
    content = file.read()
    
    # In nội dung đã đọc
    print(content)


''' Bạn là sinh viên của một trường Đại học, bạn cần đóng số tiền là 4535 đô cho học phí.
Trường đại học sẽ giảm 10% khi thanh toán sớm. Vậy khi giảm 10% số tiền đóng là bao nhiêu ?
'''

tuition = 4535
discount = 10 / 100

# Công thức tính 10% của số tiền 
money_dis = tuition * discount

print("Số tiền đã giảm 10% là:", money_dis, "$")
print("Số tiền phải đóng là:", tuition - money_dis, "$")
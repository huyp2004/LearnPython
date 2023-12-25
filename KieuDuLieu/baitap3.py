# Nhap vao ten cuar ban, duoc cach nhau bang dau "--". Vd: "Nguyen--Van--A"

temp = ["Ten", "cua", "ban", "la"]
name = input("Nhap vao ten cua ban: ")

for i in temp:
    print(i, end="--")

print(name)
results = []
n = 160
sums = {}
# duyệt qua tất cả các cặp số (a, b) và tính tổng của chúng, sau đó thêm kết quả vào bảng băm
for a in range(n):
    for b in range(n):
        s = a + b
        if s not in sums:
            sums[s] = [(a, b)]
            break
        else:
            sums[s].append((a, b))
            break
# duyệt qua tất cả các cặp số (c, d) và kiểm tra xem tổng của chúng có giá trị n và có tồn tại trong bảng băm không
for c in range(n):
    for d in range(n):
        s = c + d
        if n - s in sums:
            for pair in sums[n - s]:
                results.append(pair + (c, d))
                break
print(results)

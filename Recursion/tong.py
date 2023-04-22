def tong_dequy(n):
    if n == 1:
        return 1
    else:
        return n + tong_dequy(n-1)

print(tong_dequy(10))
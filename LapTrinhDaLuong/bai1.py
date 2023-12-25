from threading import Thread
import time

def myfunc(a):
    for i in range(a):
        print(i, end=' ')
        time.sleep(1)


def myfunc2(a):
    for i in range(-5, a, 1):
        print(i, end=' ')
        time.sleep(1)


a = 10
# myfunc(a)
print()
# myfunc2(a)

test_1 = Thread(target=myfunc, args=(a,))
test_2 = Thread(target=myfunc2, args=(a,))

test_1.start()
test_2.start()

test_1.join()
test_2.join()

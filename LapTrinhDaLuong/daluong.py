from concurrent.futures import thread
from threading import Thread
import threading
import time


def sorted_number():
    lst = [5, 1, 61, 25, 16, 7]
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                lst[j], lst[i] = lst[i], lst[j]
        time.sleep(0.5)
        print('Sorted 1:', i, lst)


def sorted_number2():
    lst = [4, 11, 61, 25, 1, 0]
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                lst[j], lst[i] = lst[i], lst[j]
        time.sleep(0.5)
        print('Sorted 2:', i, lst)

start = time.time()

sorted_number()
sorted_number2()

end = time.time()
elapsed = end - start
print(elapsed)

start = time.time()

number1 = threading.Thread(target=sorted_number, args=())
number1.start()

number2 = threading.Thread(target=sorted_number2, args=())
number2.start()

number1.join()
number2.join()
end = time.time()
elapsed = end - start
print(elapsed)
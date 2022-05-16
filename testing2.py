import time


def fun():
    for i in range(100000000):
        i*i


a = time.time()
fun()
b = time.time()

print(a)
print(b)
print(b-a)

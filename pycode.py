def my_func(a):
    l1 = []
    for i in a:
        l1.append(i*5)
        print(l1)
    return l1


d = [100, 200, 300]
b = my_func(d)
print(b)



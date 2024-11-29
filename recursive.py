def add(a):
    a += 1
    print(a)
    if a < 25:
        add(a)

add(1)
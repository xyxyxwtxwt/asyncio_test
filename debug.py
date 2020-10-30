def add(x, y):
    res = 0
    for _ in range(20):
        x += 1
        y += 1
        res = x + y

    return res

if __name__ == '__main__':
    res = add(1, 1)
    print(res)

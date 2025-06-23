LEN = 100_000_000


def with_initial_size():
    l = [0] * LEN
    for i in range(LEN):
        l[i] = i
    return l


def without_initial_size():
    l = []
    for i in range(LEN):
        l.append(i)
    return l


def list_comprehension():
    l = [i for i in range(LEN)]
    return l

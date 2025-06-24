class MyClass:
    def __init__(self):
        self.a = 100
        self.b = 100
        self.c = 100
        self.d = 100
        self.e = 100
        self.f = 100
        self.g = 100
        self.h = 100
        self.i = 100
        self.j = 100
        self.k = 100
        self.l = 100
        self.m = 100
        self.n = 100
        self.o = 100
        self.p = 100
        self.q = 100
        self.r = 100
        self.s = 100
        self.t = 100
        self.u = 100
        self.v = 100
        self.w = 100
        self.x = 100
        self.y = 100
        self.z = 100


OBJECT_COUNT = 1000000
objects = [MyClass() for _ in range(OBJECT_COUNT)]


def readable():
    for obj in objects:
        obj.a += 1
        obj.b += 1
        obj.c += 1
        obj.d += 1
        obj.e += 1
        obj.f += 1
        obj.g += 1
        obj.h += 1
        obj.i += 1
        obj.j += 1
        obj.k += 1
        obj.l += 1
        obj.m += 1
        obj.n += 1
        obj.o += 1
        obj.p += 1
        obj.q += 1
        obj.r += 1
        obj.s += 1
        obj.t += 1
        obj.u += 1
        obj.v += 1
        obj.w += 1
        obj.x += 1
        obj.y += 1
        obj.z += 1


def per_object():
    for obj in objects:
        for attr in (
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ):
            setattr(obj, attr, getattr(obj, attr) + 1)


def per_attr():
    for attr in (
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ):
        for obj in objects:
            setattr(obj, attr, getattr(obj, attr) + 1)

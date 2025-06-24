import gc


ITERS = 200_000_000


def make_objects():
    objects = []
    for _ in range(ITERS):
        objects.append(object())
    return objects


def with_gc():
    return make_objects()


def without_gc():
    try:
        gc.disable()
        return make_objects()
    finally:
        gc.enable()

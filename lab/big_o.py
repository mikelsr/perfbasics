import bisect


LEN = 100_000_000
ITEMS = [i for i in range(LEN)]
LOOKUPS = [421, 540_354, 29_233_421, 99_999_999, 1, 50_000_000, 63_312_512]

LIST = [i for i in range(LEN)]
SET = {i for i in range(LEN)}


def search_list():
    for item in LOOKUPS:
        assert item in LIST


def search_sorted_list():
    for item in LOOKUPS:
        i = bisect.bisect_left(LIST, item)
        assert i < LEN and LIST[i] == item


def search_set():
    for item in LOOKUPS:
        assert item in SET

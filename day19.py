from functools import cache


def parse(text):
    tst, gst = text.split("\n\n")
    ts = tst.split(", ")
    gs = gst.split("\n")
    return tuple(ts), gs


@cache
def is_possible(ts, g):
    if g == "":
        return 1
    n = 0
    for t in ts:
        if g[: len(t)] == t:
            n += is_possible(ts, g[len(t) :])
    return n


def num_possible(ts, gs):
    return sum(1 for g in gs if is_possible(ts, g))


def sum_possible(ts, gs):
    return sum(is_possible(ts, g) for g in gs)


if __name__ == "__main__":
    with open("day19.txt") as f:
        ts, gs = parse(f.read().strip())
    print(num_possible(ts, gs))
    print(sum_possible(ts, gs))

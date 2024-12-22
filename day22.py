import functools
import itertools


def parse(text):
    return [int(n) for n in text.split("\n")]


def secret(n):
    n = n ^ (n << 6) % 16777216
    n = n ^ (n >> 5) % 16777216
    n = n ^ (n << 11) % 16777216
    return n


def sum_secret_nums(nums):
    s = 0
    for num in nums:
        n = num
        for _ in range(2000):
            n = secret(n)
        s += n
    return s


def diffs(nums):
    seqs = []
    for num in nums:
        n = num
        diff_seq = []
        price_seq = []
        for _ in range(2000):
            n_ = secret(n)
            diff_seq.append(n_ % 10 - n % 10)
            price_seq.append(n % 10)
            n = n_
        seqs.append((diff_seq, price_seq))
    return seqs


def best_seq(nums):
    ds = diffs(nums)
    diff_maps = []
    for d, p in ds:
        diff_map = {}
        for i in range(2000 - 5):
            diff = tuple(d[i : i + 4])
            n = p[i + 4]
            if diff not in diff_map:
                diff_map[diff] = n
        diff_maps.append(diff_map)
    m = -1
    for i in range(-9, 9):
        for j in range(-9, 9):
            for k in range(-9, 9):
                for l in range(-9, 9):
                    n = 0
                    for diff_map in diff_maps:
                        diff = (i, j, k, l)
                        n += diff_map.get(diff, 0)
                    m = max(n, m)
    return m


if __name__ == "__main__":
    with open("day22.txt") as f:
        nums = parse(f.read().strip())
    print(sum_secret_nums(nums))
    print(best_seq([1, 2, 3, 2024]))
    print(best_seq(nums))

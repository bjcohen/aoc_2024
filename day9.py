import itertools


def checksum(blocks):
    blocks = blocks.copy()
    i = 0
    cs = 0
    filled = 0
    last_i = (len(blocks) - 1) // 2
    while i <= last_i:
        block = blocks[2 * i]
        free = blocks[2 * i + 1]
        cs += i * (
            ((filled + block - 1) * (filled + block) // 2)
            - ((filled - 1) * filled // 2)
        )
        filled += block
        while free > 0 and i < last_i:
            last_block = blocks[last_i * 2]
            if last_block > free:
                cs += last_i * (
                    (
                        (filled + free - 1) * (filled + free) // 2
                        - (filled * (filled - 1) // 2)
                    )
                )
                blocks[last_i * 2] = last_block - free
                filled += free
                free = 0
            else:
                cs += last_i * (
                    (
                        (filled + last_block - 1) * (filled + last_block) // 2
                        - (filled * (filled - 1) // 2)
                    )
                )
                blocks[last_i * 2] = 0
                filled += last_block
                free -= last_block
                last_i -= 1
        i += 1
    return cs


def checksum_nofrag(blocks):
    blocks = blocks.copy()
    bs = []
    for i in range(len(blocks) // 2):
        bs.append((i, blocks[2 * i], blocks[2 * i + 1]))
    bs.append((len(blocks) // 2, blocks[-1], 0))
    i = len(bs) - 1
    while i >= 0:
        n, b, f = bs[i]
        for j in range(min(len(bs) - 1, i)):
            n_, b_, f_ = bs[j]
            if bs[j][2] >= b:
                bs.pop(i)
                bs[j] = (n_, b_, 0)
                bs.insert(j + 1, (n, b, f_ - b))
                n__, b__, f__ = bs[i]
                bs[i] = n__, b__, f__ + b + f
                break
        else:
            i -= 1
    filled = 0
    cs = 0
    for n, b, f in bs:
        cs += n * ((filled + b - 1) * (filled + b) // 2 - (filled - 1) * filled // 2)
        filled += b + f
    return cs


if __name__ == "__main__":
    with open("day9.txt") as f:
        blocks = [int(n) for n in f.read().strip()]
    print(checksum(list([int(n) for n in "2333133121414131402"])))
    print(checksum_nofrag(list([int(n) for n in "2333133121414131402"])))
    print(checksum(blocks))
    print(checksum_nofrag(blocks))

import heapq


def parse(text):
    return [
        (int(row[0]), int(row[1]))
        for row in (row.split(",") for row in text.split("\n"))
    ]


def min_path(bs, n):
    bs = set(bs)
    queue = [(0, 0, 0)]
    seen = set()
    while queue:
        d, x, y = heapq.heappop(queue)
        if (x, y) == (n, n):
            return d
        if (x, y) in seen:
            continue
        seen.add((x, y))
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx <= n and ny >= 0 and ny <= n and (nx, ny) not in bs:
                heapq.heappush(queue, (d + 1, nx, ny))


def first_impassable(bs, n):
    for i in range(len(bs) + 1):
        if min_path(bs[:i], n) is None:
            return bs[i - 1]


if __name__ == "__main__":
    with open("day18.txt") as f:
        bs = parse(f.read().strip())
    print(min_path(bs[:1024], 70))
    print(first_impassable(bs, 70))

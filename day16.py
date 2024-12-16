import heapq


def parse(f):
    grid = [row.strip() for row in f]
    return grid


def min_path(grid):
    y = len(grid) - 2
    x = 1
    d = ">"
    queue = [(0, x, y, d)]
    seen = {}
    while queue:
        l, x, y, d = heapq.heappop(queue)
        if (x, y, d) in seen:
            continue
        seen[x, y, d] = l
        for nl, nd in {
            ">": ((l + 1, ">"), (l + 1001, "v"), (l + 1001, "^")),
            "<": ((l + 1, "<"), (l + 1001, "v"), (l + 1001, "^")),
            "^": ((l + 1, "^"), (l + 1001, "<"), (l + 1001, ">")),
            "v": ((l + 1, "v"), (l + 1001, "<"), (l + 1001, ">")),
        }[d]:
            nx, ny = {
                ">": (x + 1, y),
                "v": (x, y + 1),
                "<": (x - 1, y),
                "^": (x, y - 1),
            }[nd]
            if grid[ny][nx] in [".", "E"]:
                heapq.heappush(queue, (nl, nx, ny, nd))
    sl = 1e100
    queue = []
    for d in [">", "<", "^", "v"]:
        e = (len(grid[0]) - 2, 1, d)
        if e in seen:
            if seen[e] < sl:
                sl = seen[e]
                queue.append((sl, *e))
    on_path = set()
    while queue:
        l, x, y, d = queue.pop(0)
        on_path.add((x, y))
        for pl, pd in {
            ">": ((l - 1, ">"), (l - 1001, "v"), (l - 1001, "^")),
            "<": ((l - 1, "<"), (l - 1001, "v"), (l - 1001, "^")),
            "^": ((l - 1, "^"), (l - 1001, "<"), (l - 1001, ">")),
            "v": ((l - 1, "v"), (l - 1001, "<"), (l - 1001, ">")),
        }[d]:
            px, py = {
                ">": (x - 1, y),
                "v": (x, y - 1),
                "<": (x + 1, y),
                "^": (x, y + 1),
            }[d]
            if seen.get((px, py, pd), None) == pl:
                queue.append((pl, px, py, pd))
    return sl, len(on_path)


if __name__ == "__main__":
    with open("day16.txt") as f:
        grid = parse(f)
    path_length, n_cells = min_path(grid)
    print(path_length)
    print(n_cells)

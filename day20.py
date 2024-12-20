import heapq
import itertools


def parse(text):
    return [[c for c in row] for row in text.split("\n")]


def n_cheats(grid):
    sy = [i for i, row in enumerate(grid) if "S" in row][0]
    sx = grid[sy].index("S")
    h = len(grid)
    w = len(grid[0])
    queue = [(0, sx, sy, [(sx, sy)])]
    seen = set()
    paths = []
    while queue:
        d, x, y, path = heapq.heappop(queue)
        if grid[y][x] == "E":
            paths.append(path)
        # if (x, y) in seen:
        #     continue
        # seen.add((x, y))
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if grid[ny][nx] != "#" and (nx, ny) not in path:
                heapq.heappush(queue, (d + 1, nx, ny, path + [(nx, ny)]))

    cheats = {}
    for path in paths:
        for i, (x, y) in enumerate(path):
            for dx, dy, dx_, dy_ in [
                (-2, 0, -1, 0),
                (2, 0, 1, 0),
                (0, -2, 0, -1),
                (0, 2, 0, 1),
            ]:
                nx, ny = x + dx, y + dy
                if (
                    nx >= 0
                    and nx < w
                    and ny >= 0
                    and ny < h
                    and grid[ny][nx] in [".", "E"]
                    and (nx, ny) in path
                ):
                    ni = path.index((nx, ny))
                    l = ni - i - 2
                    if l > 0:
                        cheats[l] = cheats.get(l, 0) + 1
    cheats2 = {}
    for path in paths:
        for i, (xi, yi) in enumerate(path):
            for j, (xj, yj) in enumerate(path):
                skip = abs(yi - yj) + abs(xi - xj)
                if skip <= 20 and j - i - skip > 0:
                    cheats2[xi, yi, xj, yj] = j - i - skip
    return sum(i for n, i in cheats.items() if n >= 100), sum(
        1 for xs, n in cheats2.items() if n >= 100
    )


if __name__ == "__main__":
    with open("day20.txt") as f:
        grid = parse(f.read().strip())
    test_grid = parse(
        """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
    """.strip()
    )
    print(n_cheats(test_grid))
    print(n_cheats(grid))

if __name__ == "__main__":
    with open("day6.txt") as f:
        grid = [[c for c in row.strip()] for row in f]
    for yi, row in enumerate(grid):
        for xi, c in enumerate(row):
            if c == "^":
                xs, ys = xi, yi
    d = "^"
    x, y = xs, ys
    seen = set()
    while x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid):
        seen.add((x, y))
        dx, dy = {
            "^": (0, -1),
            "v": (0, 1),
            "<": (-1, 0),
            ">": (1, 0),
        }[d]
        try:
            if grid[y + dy][x + dx] == "#":
                d = {
                    "^": ">",
                    "v": "<",
                    "<": "^",
                    ">": "v",
                }[d]
            else:
                x, y = x + dx, y + dy
        except IndexError:
            break
    print(len(seen))

    found_cycle = 0
    for yi in range(len(grid)):
        for xi in range(len(grid[0])):
            if grid[yi][xi] == "#":
                continue
            x, y, d = xs, ys, "^"
            seen = set()
            while x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid):
                if (x, y, d) in seen:
                    found_cycle += 1
                    break
                seen.add((x, y, d))
                dx, dy = {
                    "^": (0, -1),
                    "v": (0, 1),
                    "<": (-1, 0),
                    ">": (1, 0),
                }[d]
                try:
                    if grid[y + dy][x + dx] == "#" or (x + dx == xi and y + dy == yi):
                        d = {
                            "^": ">",
                            "v": "<",
                            "<": "^",
                            ">": "v",
                        }[d]
                    else:
                        x, y = x + dx, y + dy
                except IndexError:
                    break
    print(found_cycle)

def total_price(grid, bulk=False):
    perims = {}
    areas = {}
    sides = {}
    seen = set()
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            area = 0
            perim = 0
            queue = [(x, y)]
            areas[x, y] = 0
            perims[x, y] = 0
            sides[x, y] = 0
            while queue:
                xi, yi = queue.pop()
                if (xi, yi) in seen:
                    continue
                perim = 0
                adjacents = []
                for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    x_, y_ = xi + dx, yi + dy
                    if (
                        x_ >= 0
                        and x_ < len(row)
                        and y_ >= 0
                        and y_ < len(grid)
                        and grid[y_][x_] == c
                    ):
                        if (x_, y_) not in seen:
                            queue.append((x_, y_))
                        adjacents.append((dx, dy))
                n_adjacents = len(adjacents)
                if n_adjacents == 0:
                    sides[x, y] += 4
                elif n_adjacents == 1:
                    sides[x, y] += 2
                elif n_adjacents == 2:
                    (dx1, dy1), (dx2, dy2) = adjacents
                    if (dx1 + dx2, dy1 + dy2) != (0, 0):
                        if grid[yi + dy1 + dy2][xi + dx1 + dx2] == c:
                            sides[x, y] += 1
                        else:
                            sides[x, y] += 2
                elif n_adjacents == 3:
                    if (-1, 0) not in adjacents:
                        if grid[yi + 1][xi + 1] != c:
                            sides[x, y] += 1
                        if grid[yi - 1][xi + 1] != c:
                            sides[x, y] += 1
                    elif (1, 0) not in adjacents:
                        if grid[yi + 1][xi - 1] != c:
                            sides[x, y] += 1
                        if grid[yi - 1][xi - 1] != c:
                            sides[x, y] += 1
                    elif (0, -1) not in adjacents:
                        if grid[yi + 1][xi + 1] != c:
                            sides[x, y] += 1
                        if grid[yi + 1][xi - 1] != c:
                            sides[x, y] += 1
                    elif (0, 1) not in adjacents:
                        if grid[yi - 1][xi + 1] != c:
                            sides[x, y] += 1
                        if grid[yi - 1][xi - 1] != c:
                            sides[x, y] += 1
                elif n_adjacents == 4:
                    for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                        if grid[yi + dy][xi + dx] != c:
                            sides[x, y] += 1
                areas[x, y] += 1
                perims[x, y] += 4 - n_adjacents
                seen.add((xi, yi))
    assert len(areas) == len(perims)
    total = 0
    # print(areas)
    # print(sides)
    for xy in areas:
        if bulk:
            total += areas[xy] * sides[xy]
        else:
            total += areas[xy] * perims[xy]
    return total


if __name__ == "__main__":
    with open("day12.txt") as f:
        grid = [row.strip() for row in f]
    test_grid = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
""".strip().split(
        "\n"
    )
    print(total_price(test_grid))
    print(total_price(grid))
    print(total_price(test_grid, bulk=True))
    print(total_price(grid, bulk=True))

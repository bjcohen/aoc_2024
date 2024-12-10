def trailhead_terminals(grid, x, y, distinct):
    n = grid[y][x]
    if n == 9:
        if distinct:
            return 1
        else:
            return set([(x, y)])
    if distinct:
        count = 0
    else:
        count = set()
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if (
            x + dx >= 0
            and x + dx < len(grid[0])
            and y + dy >= 0
            and y + dy < len(grid)
            and grid[y + dy][x + dx] == n + 1
        ):
            if distinct:
                count += trailhead_terminals(grid, x + dx, y + dy, distinct)
            else:
                count.update(trailhead_terminals(grid, x + dx, y + dy, distinct))
    return count


def sum_trailheads(grid, distinct=False):
    total = 0
    for y, row in enumerate(grid):
        for x, n in enumerate(row):
            if n == 0:
                if distinct:
                    total += trailhead_terminals(grid, x, y, distinct)
                else:
                    terms = trailhead_terminals(grid, x, y, distinct)
                    total += len(terms)
    return total


if __name__ == "__main__":
    with open("day10.txt") as f:
        grid = [[int(c) for c in row.strip()] for row in f]
    test_grid = [
        [int(c) if c != "." else -1 for c in row.strip()]
        for row in """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""".split(
            "\n"
        )
    ]
    print(sum_trailheads(test_grid, False))
    print(sum_trailheads(grid, False))
    print(sum_trailheads(test_grid, True))
    print(sum_trailheads(grid, True))

import itertools

if __name__ == "__main__":
    with open("day8.txt") as f:
        grid = [row.strip() for row in f]
    antennas = {}
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c != ".":
                antennas[c] = antennas.get(c, [])
                antennas[c].append((x, y))

    h = len(grid)
    w = len(grid[0])

    antinodes = set()
    for a, xys in antennas.items():
        for (x1, y1), (x2, y2) in itertools.combinations(xys, 2):
            dx, dy = x2 - x1, y2 - y1
            if x1 - dx >= 0 and x1 - dx < w and y1 - dy >= 0 and y1 - dy < h:
                antinodes.add((x1 - dx, y1 - dy))
            if x2 + dx >= 0 and x2 + dx < w and y2 + dy >= 0 and y2 + dy < h:
                antinodes.add((x2 + dx, y2 + dy))
    print(len(antinodes))

    antinodes = set()
    for a, xys in antennas.items():
        for (x1, y1), (x2, y2) in itertools.combinations(xys, 2):
            dx, dy = x2 - x1, y2 - y1
            x, y = x1, y1
            while x >= 0 and x < w and y >= 0 and y < h:
                antinodes.add((x, y))
                x -= dx
                y -= dy
            x, y = x2, y2
            while x >= 0 and x < w and y >= 0 and y < h:
                antinodes.add((x, y))
                x += dx
                y += dy

    print(len(antinodes))

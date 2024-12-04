if __name__ == "__main__":
    with open("day4.txt") as f:
        ws = f.read().strip().split("\n")
    w, h = len(ws[0]), len(ws)
    count = 0
    for y in range(h):
        for x in range(w):
            for dx, dy in [
                (-1, 0),
                (1, 0),
                (0, 1),
                (0, -1),
                (-1, -1),
                (-1, 1),
                (1, 1),
                (1, -1),
            ]:
                if (
                    sum(
                        1
                        for i, c in zip(range(4), "XMAS")
                        if y + i * dy >= 0
                        and y + i * dy < h
                        and x + i * dx >= 0
                        and x + i * dx < w
                        and ws[y + i * dy][x + i * dx] == c
                    )
                    == 4
                ):
                    count += 1

    print(count)

    count = 0
    dirs = [
        (-1, 1),
        (-1, -1),
        (1, -1),
        (1, 1),
    ]
    for y in range(h):
        for x in range(w):
            if x > 0 and x < w - 1 and y > 0 and y < h - 1:
                if ws[y][x] == "A" and all(
                    ws[y + dy][x + dx] == c for (dx, dy), c in zip(dirs, "MMSS")
                ):
                    count += 1
                if ws[y][x] == "A" and all(
                    ws[y + dy][x + dx] == c
                    for (dx, dy), c in zip(dirs[1:] + dirs[:1], "MMSS")
                ):
                    count += 1
                if ws[y][x] == "A" and all(
                    ws[y + dy][x + dx] == c
                    for (dx, dy), c in zip(dirs[2:] + dirs[:2], "MMSS")
                ):
                    count += 1
                if ws[y][x] == "A" and all(
                    ws[y + dy][x + dx] == c
                    for (dx, dy), c in zip(dirs[3:] + dirs[:3], "MMSS")
                ):
                    count += 1

    print(count)

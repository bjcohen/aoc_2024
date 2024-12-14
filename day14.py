import re

h = 103
w = 101


def parse(f):
    return [
        (int(m[1]), int(m[2]), int(m[3]), int(m[4]))
        for m in (re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", l) for l in f)
    ]


def safety_rating(pss):
    q1, q2, q3, q4 = 0, 0, 0, 0
    for x, y, _, _ in pss:
        if x < w // 2 and y < h // 2:
            q1 += 1
        elif x < w // 2 and y > h // 2:
            q2 += 1
        elif x > w // 2 and y < h // 2:
            q3 += 1
        elif x > w // 2 and y > h // 2:
            q4 += 1
    return q1 * q2 * q3 * q4


def print_pss(pss):
    grid = [[" " for _ in range(w)] for _ in range(h)]
    for x, y, _, _ in pss:
        grid[y][x] = "#"
    print("\n".join("".join(row) for row in grid))


def sim(pss, n_iter, return_min=False):
    min_sr = 1e100
    min_i = None
    for i in range(n_iter):
        pss = [((x + vx) % w, (y + vy) % h, vx, vy) for (x, y, vx, vy) in pss]
        if return_min:
            sr = safety_rating(pss)
            if sr < min_sr:
                min_sr = sr
                min_i = i
                print_pss(pss)
    if return_min:
        return min_i
    else:
        return safety_rating(pss)


if __name__ == "__main__":
    with open("day14.txt") as f:
        positions = parse(f)
    print(sim(positions, 100))
    print(sim(positions, 10000, return_min=True))

import functools


def parse(text):
    return text.split("\n")


p_numeric = {
    "A": (2, 3),
    "0": (1, 3),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
}

p_directional = {
    "^": (1, 0),
    "A": (2, 0),
    "<": (0, 1),
    "v": (1, 1),
    ">": (2, 1),
}


@functools.cache
def seq_directional(src, dst, level, num_robots):
    if src == dst:
        return 1
    cx, cy = p_directional[src]
    nx, ny = p_directional[dst]
    dx, dy = nx - cx, ny - cy
    if level == num_robots - 1:
        return abs(dx) + abs(dy) + 1
    dirx = "<" if dx < 0 else ">"
    diry = "^" if dy < 0 else "v"
    if cx == 0 and ny == 0:
        cands = ["A" + dirx * abs(dx) + diry * abs(dy) + "A"]
    elif cy == 0 and nx == 0:
        cands = ["A" + diry * abs(dy) + dirx * abs(dx) + "A"]
    else:
        cands = ["A" + dirx * abs(dx) + diry * abs(dy) + "A"]
        if dy and dx:
            cands.append("A" + diry * abs(dy) + dirx * abs(dx) + "A")
    cand_steps = []
    for cand in cands:
        steps = 0
        for i in range(len(cand) - 1):
            steps += seq_directional(cand[i], cand[i + 1], level + 1, num_robots)
        cand_steps.append(steps)
    return min(cand_steps)


def seq_numeric(code, num_robots):
    c = "A"
    cands = ["A"]
    for n in code:
        new_cands = []
        cx, cy = p_numeric[c]
        nx, ny = p_numeric[n]
        dx, dy = nx - cx, ny - cy
        dirx = "<" if dx < 0 else ">"
        diry = "^" if dy < 0 else "v"
        for cand in cands:
            if cy == 3 and nx == 0:
                new_cands.append(cand + diry * abs(dy) + dirx * abs(dx) + "A")
            elif cx == 0 and ny == 3:
                new_cands.append(cand + dirx * abs(dx) + diry * abs(dy) + "A")
            else:
                new_cands.append(cand + dirx * abs(dx) + diry * abs(dy) + "A")
                if dy and dx:
                    new_cands.append(cand + diry * abs(dy) + dirx * abs(dx) + "A")
        cands = new_cands
        c = n
    return min(
        sum(
            seq_directional(cand[i], cand[i + 1], 0, num_robots)
            for i in range(len(cand) - 1)
        )
        for cand in cands
    )


def sum_complexities(codes, num_robots):
    s = 0
    for code in codes:
        s += seq_numeric(code, num_robots) * int(code[:3])
    return s


if __name__ == "__main__":
    with open("day21.txt") as f:
        codes = parse(f.read().strip())
    print(sum_complexities(["029A", "980A", "179A", "456A", "379A"], 2))
    print(sum_complexities(codes, 2))
    print(sum_complexities(codes, 25))

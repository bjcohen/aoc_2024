def eval_eq(xs, n):
    if len(xs) == 1:
        return xs[0] == n
    else:
        xs1 = xs[1:]
        xs1[0] *= xs[0]
        xs2 = xs[1:]
        xs2[0] += xs[0]
        xs3 = xs[1:]
        xs3[0] = int(str(xs[0]) + str(xs[1]))
        return eval_eq(xs1, n) or eval_eq(xs2, n) or eval_eq(xs3, n)


if __name__ == "__main__":
    with open("day7.txt") as f:
        eqs = [
            (int(l[0]), [int(n) for n in l[1].split(" ")])
            for l in (l.strip().split(": ") for l in f)
        ]
    total = 0
    for n, xs in eqs:
        if eval_eq(xs, n):
            total += n
    print(total)

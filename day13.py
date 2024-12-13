import re


def parse(text):
    return [
        [int(n) for n in ns]
        for ns in re.findall(
            r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)",
            text,
        )
    ]


def min_tokens(ms, pt2=False):
    total = 0
    for xa, ya, xb, yb, xp, yp in ms:
        if pt2:
            xp, yp = xp + 10000000000000, yp + 10000000000000
        a_det = xp * yb - xb * yp
        b_det = xa * yp - xp * ya
        co_det = xa * yb - xb * ya
        if a_det % co_det == 0 and b_det % co_det == 0:
            total += 3 * a_det // co_det + b_det // co_det
    return total


if __name__ == "__main__":
    with open("day13.txt") as f:
        machines = parse(f.read())
    test_machines = parse(
        """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""
    )
    print(min_tokens(test_machines))
    print(min_tokens(machines))
    print(min_tokens(test_machines, pt2=True))
    print(min_tokens(machines, pt2=True))

import re


if __name__ == "__main__":
    with open("day3.txt") as f:
        instrs = f.read().strip()
    result = 0
    for m in re.finditer(r"mul\((\d+),(\d+)\)", instrs):
        result += int(m[1]) * int(m[2])
    print(result)
    result = 0
    enabled = True
    for m in re.finditer(r"(mul|do|don\'t)\(((\d+),(\d+))?\)", instrs):
        if m[1] == "mul" and enabled:
            result += int(m[3]) * int(m[4])
        elif m[1] == "do":
            enabled = True
        elif m[1] == "don't":
            enabled = False
    print(result)

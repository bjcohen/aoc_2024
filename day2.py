def is_safe(line):
    incdec = None
    safe = True
    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            safe = False
            break
        elif line[i] < line[i + 1]:
            if incdec is None:
                incdec = "inc"
            elif incdec == "dec":
                safe = False
                break
            diff = abs(line[i] - line[i + 1])
            if diff < 1 or diff > 3:
                safe = False
                break
        else:
            if incdec is None:
                incdec = "dec"
            elif incdec == "inc":
                safe = False
                break
            diff = abs(line[i] - line[i + 1])
            if diff < 1 or diff > 3:
                safe = False
                break
    return safe


if __name__ == "__main__":
    with open("day2.txt") as f:
        report = [[int(n) for n in l.split()] for l in f.read().strip().split("\n")]
    safecnt = 0
    for line in report:
        if is_safe(line):
            safecnt += 1
    print(safecnt)
    safecnt2 = 0
    for line in report:
        any_safe = False
        for i in range(len(line)):
            if is_safe(line[0:i] + line[i + 1 :]):
                any_safe = True
        if any_safe:
            safecnt2 += 1
    print(safecnt2)

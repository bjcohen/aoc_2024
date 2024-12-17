import re


def parse(text):
    a = int(re.search(r"Register A: (\d+)", text)[1])
    b = int(re.search(r"Register B: (\d+)", text)[1])
    c = int(re.search(r"Register C: (\d+)", text)[1])
    prog = [int(i) for i in re.search(r"Program: ([\d,]+)", text)[1].split(",")]
    return prog, a, b, c


def run(prog, a, b, c):
    ip = 0

    def combo(op):
        assert op >= 0 and op < 7, f"op must be between 0 and 7, but was {op}"
        if op < 4:
            return op
        return {
            4: a,
            5: b,
            6: c,
        }[op]

    while ip < len(prog):
        instr = prog[ip]
        op = prog[ip + 1]
        if instr == 0:
            a = a // (2 ** combo(op))
        elif instr == 1:
            b = b ^ op
        elif instr == 2:
            b = combo(op) % 8
        elif instr == 3:
            if a != 0:
                ip = op
        elif instr == 4:
            b = b ^ c
        elif instr == 5:
            yield combo(op) % 8
        elif instr == 6:
            b = a // (2 ** combo(op))
        elif instr == 7:
            c = a // (2 ** combo(op))
        else:
            raise RuntimeException(f"unhandled op {op}")
        if instr != 3 or a == 0:
            ip += 2


if __name__ == "__main__":
    with open("day17.txt") as f:
        prog, a, b, c = parse(f.read())
    print(",".join(str(i) for i in run(prog, a, b, c)))
    a = 0
    for n in range(len(prog)):
        for i in range(100):
            if list(run(prog, a * 8 + i, b, c)) == prog[-(n + 1) :]:
                a = a * 8 + i
                break
        else:
            print("couldn't find")
    print(a)
    print(list(run(prog, a, b, c)))

# b = a & 7
# b = b ^ 1
# c = a >> b
# b = b ^ 5
# b = b ^ c
# output b & 7
# a = a >> 3
# if a != 0, goto 0

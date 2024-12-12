def run(n, ss):
    ss = {s: 1 for s in ss}
    for i in range(n):
        ss_ = {}
        for s, count in ss.items():
            if s == 0:
                if 1 not in ss_:
                    ss_[1] = 0
                ss_[1] += count
            elif len(str(s)) % 2 == 0:
                str_s = str(s)
                s1 = int(str_s[: len(str_s) // 2])
                s2 = int(str_s[len(str_s) // 2 :])
                if s1 not in ss_:
                    ss_[s1] = 0
                if s2 not in ss_:
                    ss_[s2] = 0
                ss_[s1] += count
                ss_[s2] += count
            else:
                if s * 2024 not in ss_:
                    ss_[s * 2024] = 0
                ss_[s * 2024] += count
        ss = ss_
    return sum(ss.values())


if __name__ == "__main__":
    with open("day11.txt") as f:
        ss = [int(s) for s in f.read().strip().split()]
    print(run(25, ss))
    print(run(75, ss))

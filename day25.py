if __name__ == "__main__":
    with open("day25.txt") as f:
        text = f.read()
    locks = []
    keys = []
    for thing in text.split("\n\n"):
        grid = thing.split("\n")
        heights = []
        if grid[0] == "#####":
            for i in range(5):
                for j in range(7):
                    if grid[j][i] != "#":
                        heights.append(j)
                        break
            locks.append(heights)
        elif grid[6] == "#####":
            for i in range(5):
                for j in range(7):
                    if grid[6 - j][i] != "#":
                        heights.append(j)
                        break
            keys.append(heights)

    count = sum(
        1
        for lock in locks
        for key in keys
        if all(l + k <= 7 for l, k in zip(lock, key))
    )
    print(count)

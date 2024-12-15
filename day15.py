import itertools


def parse(f):
    grid_str, moves_str = f.split("\n\n")
    grid = [[c for c in row.strip()] for row in grid_str.split("\n")]
    moves = "".join(moves_str.split("\n"))
    return grid, moves


def widen(grid):
    return [
        list(
            itertools.chain.from_iterable(
                {"#": "##", "O": "[]", ".": "..", "@": "@."}[c] for c in row
            )
        )
        for row in grid
    ]


def gps(grid):
    return sum(
        100 * y + x
        for y, row in enumerate(grid)
        for x, c in enumerate(row)
        if c in ["O", "["]
    )


def move(grid, x, y, dx, dy, do_move=False):
    if dx:
        nb = 0
        while grid[y][x + nb * dx + dx] in ["O", "[", "]"]:
            nb += 1
        ncell = grid[y][x + nb * dx + dx]
        assert ncell in [".", "#"], f"unexpected value for ncell [{ncell}]"
        can_move = ncell == "."
        if can_move and do_move:
            grid[y][x + nb * dx], grid[y][x + nb * dx + dx] = (
                grid[y][x + nb * dx + dx],
                grid[y][x + nb * dx],
            )
            for i in range(nb):
                grid[y][x + (nb - i - 1) * dx], grid[y][x + (nb - i) * dx] = (
                    grid[y][x + (nb - i) * dx],
                    grid[y][x + (nb - i - 1) * dx],
                )
        return can_move
    elif dy:
        ncell = grid[y + dy][x]
        if ncell == ".":
            if do_move:
                grid[y + dy][x], grid[y][x] = grid[y][x], grid[y + dy][x]
            return True
        if ncell == "O":
            can_move = move(grid, x, y + dy, dx, dy, do_move)
            if can_move and do_move:
                grid[y + dy][x], grid[y][x] = grid[y][x], grid[y + dy][x]
            return can_move
        if ncell == "#":
            return False
        if ncell == "[":
            can_move = move(grid, x, y + dy, dx, dy, do_move) and move(
                grid, x + 1, y + dy, dx, dy, do_move
            )
            if can_move and do_move:
                grid[y + dy][x], grid[y][x] = grid[y][x], grid[y + dy][x]
            return can_move
        if ncell == "]":
            can_move = move(grid, x, y + dy, dx, dy, do_move) and move(
                grid, x - 1, y + dy, dx, dy, do_move
            )
            if can_move and do_move:
                grid[y + dy][x], grid[y][x] = grid[y][x], grid[y + dy][x]
            return can_move
        raise RuntimeError(f"unexpected ncell {ncell}")
    raise RuntimeError(f"expected dx or dy, but got {dx}, {dy}")


def sim(grid, moves, wide=False):
    if wide:
        grid = widen(grid)
    else:
        grid = [row.copy() for row in grid]
    y = [i for i, row in enumerate(grid) if "@" in row][0]
    x = grid[y].index("@")
    for m in moves:
        dx, dy = {
            "v": (0, 1),
            "^": (0, -1),
            "<": (-1, 0),
            ">": (1, 0),
        }[m]
        if move(grid, x, y, dx, dy, False):
            move(grid, x, y, dx, dy, True)
            # print("\n".join("".join(row) for row in grid))
            x += dx
            y += dy
    return grid


if __name__ == "__main__":
    with open("day15.txt") as f:
        grid, moves = parse(f.read())
    print(
        gps(
            sim(
                *parse(
                    """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""
                )
            )
        )
    )
    print(gps(sim(grid, moves)))
    print(gps(sim(grid, moves, wide=True)))

def count_paths(grid):
    H = len(grid)
    W = len(grid[0])
    f = [0] * H
    f[0] = 1
    f[-1] = 1
    total = [0] * 26
    for r in range(H):
        total[ord(grid[r][W - 1]) - 97] += f[r]
    for c in range(W - 2, -1, -1):
        new_f = [0] * H
        for r in range(H):
            ch = ord(grid[r][c]) - 97
            val = f[r] + total[ch]
            if grid[r][c + 1] == grid[r][c]:
                val -= f[r]
            new_f[r] = val
        for r in range(H):
            total[ord(grid[r][c]) - 97] += new_f[r]
        f = new_f
    return sum(f)


def solve(path="ijones.in"):
    with open(path, "r", encoding="utf-8") as fp:
        W, H = map(int, fp.readline().split())
        grid = [fp.readline().rstrip("\n") for _ in range(H)]
    return count_paths(grid)


if __name__ == "__main__":
    print(solve())

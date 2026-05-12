import csv

INF = float("inf")


def read_matrix(path):
    matrix = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            matrix.append([float(x) for x in row])
    return matrix


def min_cable_length(matrix):
    n = len(matrix)
    if n <= 1:
        return 0
    in_tree = [False] * n
    min_edge = [INF] * n
    min_edge[0] = 0
    total = 0
    for _ in range(n):
        u = -1
        for v in range(n):
            if not in_tree[v] and (u == -1 or min_edge[v] < min_edge[u]):
                u = v
        in_tree[u] = True
        total += min_edge[u]
        for v in range(n):
            if not in_tree[v] and matrix[u][v] < min_edge[v]:
                min_edge[v] = matrix[u][v]
    return total


def solve(path="islands.csv"):
    matrix = read_matrix(path)
    return min_cable_length(matrix)


if __name__ == "__main__":
    print(solve())

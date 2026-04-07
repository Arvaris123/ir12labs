import ast


def flood_fill(matrix, row, col, replacement):
    target = matrix[row][col]
    if target == replacement:
        return matrix
    stack = [(row, col)]
    while stack:
        r, c = stack.pop()
        if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]):
            continue
        if matrix[r][c] != target:
            continue
        matrix[r][c] = replacement
        stack.append((r + 1, c))
        stack.append((r - 1, c))
        stack.append((r, c + 1))
        stack.append((r, c - 1))
    return matrix


def read_input(filename):
    with open(filename) as f:
        lines = f.readlines()
    rows, cols = lines[0].strip().split(',')
    start_row, start_col = lines[1].strip().split(',')
    replacement = lines[2].strip().strip("'")
    matrix = []
    for i in range(3, 3 + int(rows)):
        row = ast.literal_eval(lines[i].strip().rstrip(','))
        matrix.append(row)
    return matrix, int(start_row), int(start_col), replacement


def write_output(filename, matrix):
    with open(filename, 'w') as f:
        for row in matrix:
            f.write(str(row) + '\n')



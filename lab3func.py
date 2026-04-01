class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def find_successor(tree, node):
    if node.right:
        current = node.right
        while current.left:
            current = current.left
        return current
    current = node
    while current.parent and current.parent.right == current:
        current = current.parent
    return current.parent


def build_custom_tree():
    return Node(
        10,
        left=Node(
            5,
            left=Node(3, left=Node(4)),
            right=Node(7, left=Node(99, left=Node(98))),
        ),
        right=Node(
            15,
            right=Node(20, left=Node(12)),
        ),
    )


def inorder_invert(node, result=None):
    if result is None:
        result = []
    if node is None:
        return result
    inorder_invert(node.right, result)
    result.append(node.value)
    inorder_invert(node.left, result)
    return result


FILE_PATH = "tree_output.txt"


def level_order(node):
    result = []
    queue = [node]
    while queue:
        cur = queue.pop(0)
        if cur is None:
            result.append(None)
        else:
            result.append(cur.value)
            queue.append(cur.left)
            queue.append(cur.right)
    while result and result[-1] is None:
        result.pop()
    return result


def tree_from_level_order(vals):
    if not vals:
        return None
    root = Node(vals[0])
    queue = [root]
    i = 1
    while queue and i < len(vals):
        cur = queue.pop(0)
        if i < len(vals):
            if vals[i] is not None:
                cur.left = Node(vals[i])
                queue.append(cur.left)
            i += 1
        if i < len(vals):
            if vals[i] is not None:
                cur.right = Node(vals[i])
                queue.append(cur.right)
            i += 1
    return root


def write_tree(node, path=FILE_PATH):
    inv = inorder_invert(node)
    lo = level_order(node)
    with open(path, "w") as f:
        for v in inv:
            f.write(f"{v}\n")
        f.write("\n")
        for v in lo:
            f.write(f"{v}\n")


def read_tree(path=FILE_PATH):
    invert_vals = []
    level_vals = []
    section = "invert"
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                section = "level"
                continue
            val = None if line == "None" else int(line)
            if section == "invert":
                invert_vals.append(val)
            elif section == "level":
                level_vals.append(val)
    tree = tree_from_level_order(level_vals)
    return invert_vals, tree


def _render_tree_lines(root):
    if root is None:
        return []

    nodes = []

    def traverse(node, depth):
        if node is None:
            return
        traverse(node.left, depth + 1)
        nodes.append((node, len(nodes), depth))
        traverse(node.right, depth + 1)

    traverse(root, 0)

    if not nodes:
        return []

    pos = {id(n): (x, d) for n, x, d in nodes}
    max_depth = max(d for _, d in pos.values())
    max_lw = max(len(str(n.value)) for n, _, _ in nodes)
    cell_w = max(max_lw + 2, 4)
    total_width = len(nodes) * cell_w

    num_rows = (max_depth + 1) * 2 - 1
    grid = [[" "] * total_width for _ in range(num_rows)]

    def place(r, c, ch):
        if 0 <= r < num_rows and 0 <= c < total_width:
            grid[r][c] = ch

    for node, x, depth in nodes:
        label = str(node.value)
        val_row = depth * 2
        label_col = x * cell_w + (cell_w - len(label)) // 2
        for i, ch in enumerate(label):
            place(val_row, label_col + i, ch)

        center = x * cell_w + cell_w // 2
        for child, is_left in [(node.left, True), (node.right, False)]:
            if child is None:
                continue
            cx, _ = pos[id(child)]
            child_center = cx * cell_w + cell_w // 2
            branch_col = (center + child_center) // 2
            place(val_row + 1, branch_col, "/" if is_left else "\\")

    lines = ["".join(row).rstrip() for row in grid]
    while lines and not lines[-1].strip():
        lines.pop()
    return lines


def display_upside_down(root):
    lines = _render_tree_lines(root)
    if not lines:
        print("(empty tree)")
        return

    lines.reverse()
    flipped = []
    for line in lines:
        new_line = line.replace("/", "\x00").replace("\\", "/").replace("\x00", "\\")
        flipped.append(new_line)

    min_indent = min(
        (len(l) - len(l.lstrip()) for l in flipped if l.strip()), default=0
    )
    flipped = [l[min_indent:] for l in flipped]
    print("\n".join(flipped))

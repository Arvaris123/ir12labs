import heapq

INF = float("inf")


def build_graph(n, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    return graph


def dijkstra(graph, start, n):
    dist = [INF] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist


def find_min_latency(n, clients, edges):
    graph = build_graph(n, edges)
    client_set = set(clients)
    best = INF
    for node in range(1, n + 1):
        if node in client_set:
            continue
        dist = dijkstra(graph, node, n)
        worst = max(dist[c] for c in clients)
        if worst < best:
            best = worst
    return best


def parse_input(text):
    lines = text.strip().splitlines()
    n, m = map(int, lines[0].split())
    clients = list(map(int, lines[1].split()))
    edges = []
    for i in range(m):
        a, b, w = map(int, lines[2 + i].split())
        edges.append((a, b, w))
    return n, clients, edges


def solve(text):
    n, clients, edges = parse_input(text)
    return find_min_latency(n, clients, edges)


def run_files(input_path="gamsrv.in", output_path="gamsrv.out"):
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()
    answer = solve(text)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(str(answer))
    return answer

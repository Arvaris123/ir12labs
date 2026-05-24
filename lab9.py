def find_all(haystack, needle):
    m = len(needle)
    if m == 0:
        return []
    alphabet = set(haystack) | set(needle)
    table = [{} for _ in range(m + 1)]
    for state in range(m + 1):
        for ch in alphabet:
            k = min(m, state + 1)
            while k > 0 and needle[:k] != (needle[:state] + ch)[state + 1 - k:]:
                k -= 1
            table[state][ch] = k
    result = []
    state = 0
    for i, ch in enumerate(haystack):
        state = table[state].get(ch, 0)
        if state == m:
            result.append(i - m + 1)
    return result

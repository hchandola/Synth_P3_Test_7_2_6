from typing import List


def sat306(tri: List[int], edges=[[0, 17], [0, 22], [17, 22], [17, 31], [22, 31], [31, 17]]):
    a, b, c = tri
    return [a, b] in edges and [b, c] in edges and [c, a] in edges and a != b != c != a
def sol306(edges=[[0, 17], [0, 22], [17, 22], [17, 31], [22, 31], [31, 17]]):
    """Find any triangle in the given directed graph."""
    from collections import defaultdict
    outs = defaultdict(set)
    ins = defaultdict(set)
    for i, j in edges:
        if j != i:
            outs[i].add(j)
            ins[j].add(i)
    for i in outs:
        for j in outs[i]:
            try:
                if j in outs:
                    k = min(outs[j].intersection(ins[i]))
                    return [i, j, k]
            except ValueError:
                pass
# assert sat306(sol306())

import itertools


def parse(text):
    return [
        (line[0], line[1]) for line in (line.split("-") for line in text.split("\n"))
    ]


def three_links(links):
    graph = {}
    for s, d in links:
        if s not in graph:
            graph[s] = []
        if d not in graph:
            graph[d] = []
        graph[s].append(d)
        graph[d].append(s)
    edges = set(links)
    for s, d in links:
        edges.add((d, s))
    count = 0
    for s, ds in graph.items():
        for d1, d2 in itertools.combinations(ds, 2):
            if (d1, d2) in edges and (s[0] == "t" or d1[0] == "t" or d2[0] == "t"):
                count += 1

    cliques = []

    def bk1(r, p, x):
        if not p and not x:
            cliques.append(r)
        for v in list(p):
            bk1(r | set((v,)), p & set(graph[v]), x & set(graph[v]))
            p.remove(v)
            x.add(v)

    bk1(set(), set(graph.keys()), set())
    max_n = max(len(c) for c in cliques)
    max_clique = [c for c in cliques if len(c) == max_n]
    return count // 3, ",".join(sorted(max_clique[0]))


if __name__ == "__main__":
    with open("day23.txt") as f:
        links = parse(f.read().strip())
    test_links = parse(
        """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""
    )

    triples, pw = three_links(test_links)
    print(triples)
    print(pw)

    triples, pw = three_links(links)
    print(triples)
    print(pw)

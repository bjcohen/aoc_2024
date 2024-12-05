if __name__ == "__main__":
    with open("day5.txt") as f:
        rules_txt, pages_txt = f.read().strip().split("\n\n")
    rules = [[int(i) for i in r.split("|")] for r in rules_txt.split("\n")]
    pages = [[int(p) for p in line.split(",")] for line in pages_txt.split("\n")]
    smpns = 0
    incorrectly_ordered = []
    for page in pages:
        all_match = True
        for r in rules:
            try:
                if page.index(r[0]) > page.index(r[1]):
                    all_match = False
                    break
            except ValueError:
                continue
        if all_match:
            smpns += page[len(page) // 2]
        else:
            incorrectly_ordered.append(page)
    print(smpns)

    smpns2 = 0
    for page in incorrectly_ordered:
        page_init = []
        while page_init != page:
            page_init = page.copy()
            for r in rules:
                try:
                    i0 = page.index(r[0])
                    i1 = page.index(r[1])
                except ValueError:
                    continue
                if i0 > i1:
                    page[i0], page[i1] = page[i1], page[i0]
        smpns2 += page[len(page) // 2]
    print(smpns2)

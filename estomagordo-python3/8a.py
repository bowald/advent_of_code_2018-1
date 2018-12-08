def solve(d):
    l = len(d)
    total = 0
    stack = [[d[0], d[1]]]

    x = 2

    while x < l:
        children, metas = stack.pop()

        if children == 0:
            for _ in range(metas):
                total += d[x]
                x += 1
            continue
            
        children -= 1
        stack.append([children, metas])
        children = d[x]
        metas = d[x + 1]
        stack.append([children, metas])

        x += 2

    return total

with open('input_8.txt') as f:
    data = [list(map(int, line.split())) for line in f]
    print(solve(data[0]))
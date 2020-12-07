import re


def dfs(g, n, visited):
    if n not in visited:
        visited.append(n)
        if n in g:
            for v in g[n]:
                dfs(g, v, visited)
    return visited


def one_star():
    lines = open("input").read().splitlines()
    g = {}
    for line in lines:
        parent = re.findall(r"(\w+ \w+) bags contain", line)[0]
        children = re.findall(r"[1-9] (\w+ \w+)", line)
        for child in children:
            if child not in g:
                g[child] = [parent]
            else:
                g[child].append(parent)

    return len(dfs(g, "shiny gold", [])) - 1    # Remove the top "shiny gold"


def dfs2(g, n):
    ans = 0
    num = 1
    color = n
    if color != "shiny gold":
        num = int(n.split()[0])
        color = ' '.join(n.split()[1:])
    if color in g:
        for v in g[color]:
            ans += num * dfs2(g, v)
    return ans + num


def two_star():
    lines = open("input").read().splitlines()
    g = {}
    for line in lines:
        parent = re.findall(r"(\w+ \w+) bags contain", line)[0]
        children = re.findall(r"[1-9] \w+ \w+", line)
        g[parent] = children
    return dfs2(g, "shiny gold") - 1    # Remove the top "shiny gold"


if __name__ == '__main__':
    print(one_star())
    print(two_star())

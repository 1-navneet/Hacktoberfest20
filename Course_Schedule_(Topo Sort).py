from collections import defaultdict, deque

def canFinish(n, prereq):
    g = defaultdict(list)
    indeg = [0]*n
    
    for a, b in prereq:
        g[b].append(a)
        indeg[a] += 1

    q = deque([i for i in range(n) if indeg[i]==0])
    cnt = 0

    while q:
        x = q.popleft()
        cnt += 1
        for nei in g[x]:
            indeg[nei] -= 1
            if indeg[nei] == 0:
                q.append(nei)

    return cnt == n

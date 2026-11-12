from collections import deque

grid = [
    ['S', '0', '0'],
    ['1', '1', '0'],
    ['0', '0', 'G']
]

queue = deque([((0, 0), [(0, 0)])])
visited = set()

while queue:
    (x, y), path = queue.popleft()

    if (x, y) == (2, 2):
        print("Shortest Path:", path)
        print("Steps:", len(path)-1)
        break

    if (x, y) in visited:
        continue

    visited.add((x, y))

    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        nx, ny = x+dx, y+dy

        if (0 <= nx < 3 and 0 <= ny < 3
            and grid[nx][ny] != '1'
            and (nx, ny) not in visited):

            queue.append(((nx, ny), path+[(nx, ny)]))


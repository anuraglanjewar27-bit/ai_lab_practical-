from collections import deque

grid = [
    ['S', '0', '0'],
    ['1', '1', '0'],
    ['0', '0', 'G']
]

start = (0, 0)
goal = (2, 2)

queue = deque([(start, [start])])
visited = set()

while queue:
    position, path = queue.popleft()

    if position == goal:
        print("Path found:")
        print(path)
        break

    if position in visited:
        continue

    visited.add(position)

    x, y = position

    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if (0 <= nx < 3 and 0 <= ny < 3
            and grid[nx][ny] != '1'
            and (nx, ny) not in visited):

            queue.append(((nx, ny), path + [(nx, ny)]))


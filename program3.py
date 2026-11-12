import heapq

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def heuristic(state):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            goal_pos = goal.index(state[i])

            x1, y1 = i // 3, i % 3
            x2, y2 = goal_pos // 3, goal_pos % 3

            distance += abs(x1-x2) + abs(y1-y2)

    return distance


def get_moves(state):
    zero = state.index(0)
    x, y = zero // 3, zero % 3

    moves = []

    for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
        nx, ny = x+dx, y+dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_pos = nx*3 + ny

            new_state = list(state)
            new_state[zero], new_state[new_pos] = (
                new_state[new_pos], new_state[zero])

            moves.append(tuple(new_state))

    return moves


queue = [(heuristic(start), 0, start)]
visited = set()

while queue:
    f, cost, state = heapq.heappop(queue)

    if state == goal:
        print("Goal Reached!")
        print("Total Moves:", cost)
        break

    if state in visited:
        continue

    visited.add(state)

    for new_state in get_moves(state):
        if new_state not in visited:
            new_cost = cost + 1
            h = heuristic(new_state)

            heapq.heappush(
                queue, (new_cost+h, new_cost, new_state))


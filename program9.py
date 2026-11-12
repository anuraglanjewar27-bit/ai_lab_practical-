visited = set()

def dfs(a, b):

    if (a, b) in visited:
        return False

    visited.add((a, b))

    print(a, b)

    if a == 2 or b == 2:
        print("Goal Reached!")
        return True

    moves = [
        (4, b),                 # Fill jug A
        (a, 3),                 # Fill jug B
        (0, b),                 # Empty jug A
        (a, 0),                 # Empty jug B
        (a-min(a, 3-b), b+min(a, 3-b)),  # Pour A to B
        (a+min(b, 4-a), b-min(b, 4-a))   # Pour B to A
    ]

    for x, y in moves:
        if dfs(x, y):
            return True

    return False


dfs(0, 0)


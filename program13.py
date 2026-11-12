blocks = {
    'A': 'table',
    'B': 'table',
    'C': 'table'
}

holding = None
goal_stack = []

def clear(x):
    return all(blocks[b] != x for b in blocks)

def execute(action, x, y=None):
    global holding

    if action == "pickup":
        holding = x
        blocks[x] = "hand"

    elif action == "unstack":
        holding = x
        blocks[x] = "hand"

    elif action == "putdown":
        blocks[x] = "table"
        holding = None

    elif action == "stack":
        blocks[x] = y
        holding = None

    print(action, x, y if y else "")


def planner(goal_stack):

    while goal_stack:

        goal = goal_stack.pop()

        if goal[0] == "act":
            execute(goal[1], goal[2], goal[3])

        elif goal[0] == "on":
            x, y = goal[1], goal[2]

            if blocks[x] != y:
                goal_stack.append(("act", "stack", x, y))
                goal_stack.append(("holding", x))
                goal_stack.append(("clear", y))

        elif goal[0] == "holding":
            x = goal[1]

            if holding != x:
                if holding is not None:
                    goal_stack.append(("holding", x))
                    goal_stack.append(("ontable", holding))

                elif blocks[x] == "table":
                    goal_stack.append(("act", "pickup", x, None))
                    goal_stack.append(("clear", x))
                    goal_stack.append(("handempty",))

                else:
                    goal_stack.append(
                        ("act", "unstack", x, blocks[x]))
                    goal_stack.append(("clear", x))
                    goal_stack.append(("handempty",))

        elif goal[0] == "clear":
            x = goal[1]

            if not clear(x):
                for b in blocks:
                    if blocks[b] == x:
                        goal_stack.append(("ontable", b))
                        break

        elif goal[0] == "ontable":
            x = goal[1]

            if blocks[x] != "table":
                goal_stack.append(("act", "putdown", x, None))
                goal_stack.append(("holding", x))

        elif goal[0] == "handempty":
            if holding is not None:
                goal_stack.append(("ontable", holding))


# Final goal: A on B and B on C

goal_stack.append(("on", "A", "B"))
goal_stack.append(("on", "B", "C"))

planner(goal_stack)

print("Final Arrangement:")
print(blocks)


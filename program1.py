rooms = {
    'A': 'Dirty',
    'B': 'Dirty'
}

location = 'A'

while True:
    print("Location:", location)
    print("Room Status:", rooms[location])

    if rooms[location] == 'Dirty':
        print("Action: Cleaning")
        rooms[location] = 'Clean'

    elif location == 'A':
        print("Action: Move Right")
        location = 'B'

    elif location == 'B':
        print("Action: Move Left")
        location = 'A'

    if rooms['A'] == 'Clean' and rooms['B'] == 'Clean':
        print("Both rooms are clean!")
        break0


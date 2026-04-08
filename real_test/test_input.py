def main():
    # Map 20x20 initialized with None
    game_map: list[list[int | None]] = [[None for _ in range(20)] for _ in range(20)]
    turn = 0

    # Arrays for humans (soldiers + citizens) and zombies
    human_array: list[dict] = []
    zombie_array: list[dict] = []

    # Read n (number of objects) and m (number of turns)
    first_line = input().strip()
    if not first_line:
        return
    n, m = map(int, first_line.split())

    objects: list[Object] = []

    for _ in range(n):
        parts = input().strip().split()
        if len(parts) < 5:
            continue  # invalid line, skip

        id_ = int(parts[0])
        type_ = int(parts[1])
        x = int(parts[2])
        y = int(parts[3])

        obj: Object | None = None

        if type_ == 1:
            # Soldier: [ID] [Type] [x] [y] [level]
            level = int(parts[4])
            obj = Soldier(id_, type_, x, y, level)
            human_array.append(
                {"id": id_, "type": type_, "x": x, "y": y, "lvl": level}
            )
        elif type_ == 2:
            # Citizen: [ID] [Type] [x] [y] [speed] [vision]
            if len(parts) < 6:
                continue
            s = int(parts[4])
            vision = int(parts[5])
            obj = Citizen(id_, type_, x, y, s, vision)
            human_array.append(
                {"id": id_, "type": type_, "x": x, "y": y, "lvl": None}
            )
        elif type_ == 3:
            # Zombie: [ID] [Type] [x] [y] [speed]
            s = int(parts[4])
            obj = Zombie(id_, type_, x, y, s)
            zombie_array.append(
                {"id": id_, "type": type_, "x": x, "y": y}
            )

        if obj is not None:
            objects.append(obj)
            # Put id on the map if inside bounds
            if 0 <= y < 20 and 0 <= x < 20:
                game_map[y][x] = id_

    # Now you have:
    # - game_map: 20x20 grid with ids (or None)
    # - human_array: basic info for Soldier + Citizen
    # - zombie_array: basic info for Zombie
    # - objects: list of all created objects
    # - turn: current turn (starts at 0)
    # You can add turn-based simulation using these variables.


if __name__ == "__main__":
    main()
    print(objects)

class Point:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.neighbor_points = {}
        self.val = val

    def __repr__(self):
        return f"Point({self.x}, {self.y}): {self.val}"

    def add_neighbor_points(self, point, direction):
        direction_opposites = {
            'north': 'south',
            'south': 'north',
            'east': 'west',
            'west': 'east'
        }
        self.neighbor_points[direction] = point
        point.neighbor_points[direction_opposites[direction]] = self


def create_topo_map(filepath: str) -> list:
    topo_map = []
    with open(filepath, 'r') as file:
        for x, line in enumerate(file):
            points = []
            for y, val in enumerate(line.strip()):
                points.append(Point(x, y, val))
            topo_map.append(points)

    for x in range(0, len(topo_map)):
        for y in range(0, len(topo_map[0])):
            point = topo_map[x][y]

            if y > 0:
                point.add_neighbor_points(topo_map[x][y-1], 'west')
            if x > 0:
                point.add_neighbor_points(topo_map[x-1][y], 'north')
    return topo_map


def check_potential_trail(topo_map: list, position: tuple, good_trails: int) -> int | None:
    x, y = position
    point = topo_map[x][y]
    neighbors = point.neighbor_points
    for neighbor_point in neighbors:
        Neighbor = neighbors[neighbor_point]
        if int(Neighbor.val) == int(point.val) + 1:
            print(f'Recurse on point {Neighbor}')
            check_potential_trail(topo_map, (Neighbor.x, Neighbor.y), good_trails)
            return None
        elif int(point.val) == 9:
            # Reached the end of a good trail?
            print('At 9')
            return 1 + good_trails
        else:
            # Cant be good trail
            pass
    return None


def main() -> int | None:
    # Trails start on characters 0 and must go up by 1 for
    # each up/down/left/right move until 9 is reached to be considered good
    # Count the number of trails for each trail-head (0) starting point
    # and sum all of those to create the answer score
    topo_map = create_topo_map('sample_input.txt')
    print(topo_map)
    check_potential_trail(topo_map, (0, 0), 0)
    return None


if __name__ == '__main__':
    main()

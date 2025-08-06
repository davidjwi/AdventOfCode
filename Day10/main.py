class Point:
    def __init__(self, x: int, y: int, val: int):
        self.x = x
        self. y = y
        self.val = val 
        self.neighbors = {}
    
    def __repr__(self):
        return f'({self.x},{self.y}): {self.val}'
    
    def add_neighbors(self, neighborPoint: "Point", direction: str):
        # This is used to more easily link the current point to a neighbor
        # and then link the neighbor back to the current point
        direction_opposites = {
            'north': 'south',
            'south': 'north', 
            'east': 'west',
            'west': 'east'
        }
        # Create a key(direction) and value(neighborPoint) in the
        # currently-being-worked-on point's neighbor (self.neighbors) dictionary
        self.neighbors[direction] = neighborPoint 
        # Then set the neighboring point to have the current point as
        # it's neighbor in the opposite direction
        neighborPoint.neighbors[direction_opposites[direction]] = self
        

def create_map_from_file(FILEPATH: str) -> list:
    # This will be the 2D list
    topo_map = []

    with open(FILEPATH, 'r') as input_file:

        for x, row in enumerate(input_file):
            row_of_points = []
            row = row.strip()
            for y, val in enumerate(row):
                val = int(val)
                NewPoint = Point(x, y, val)
                row_of_points.append(NewPoint)

            topo_map.append(row_of_points)

    return topo_map

def link_points_to_neighbors(topo_map: list) -> list:
    # Iterate in order thru the 2d list and get the CurrPoint
    for x in range(0, len(topo_map)):
        for y in range(0, len(topo_map[0])):
            CurrPoint = topo_map[x][y]
            # This is like add/subtract to the CurrPoint's x,y coordinate
            # 'north' = -1,0 | 'south' = 1,0 | 'east' = 0,1 | 'west' = 0,-1
            # For the CurrPoint perform add_neighbors using the backward (west/applying 0,-1) point,
            # then link the backward/west point back to the current point (forward/east) 
            # Then do the same thing for looking upwards (north/applying 1,0) and
            # also link the upwards point back down/south to the current point
            # Only need to look back/west and up/north because the other directions will get linked along the way
            if y > 0:
                CurrPoint.add_neighbors(topo_map[x][y-1], 'west')
            if x > 0:
                CurrPoint.add_neighbors(topo_map[x-1][y], 'north')

    return topo_map


def modifiedDFS(CurrPoint: Point, results: list) -> list:

    neighboring_points = CurrPoint.neighbors

    for NeighborPoint in neighboring_points.values():
        #print(f'CurrPoint{CurrPoint} | NeighborVal{NeighborPoint}')
        if NeighborPoint in results:
            pass
        elif NeighborPoint.val == CurrPoint.val + 1:
            if NeighborPoint.val != 9:
                modifiedDFS(NeighborPoint, results)
            elif NeighborPoint.val == 9:
#                print(f'Full trail ends at {NeighborPoint}')
                results.append(NeighborPoint)
    return results


def main():
    FILEPATH = 'input.txt'
    topo_map = create_map_from_file(FILEPATH)
    topo_map = link_points_to_neighbors(topo_map)
    answer = 0
    for x in range(0, len(topo_map)):
        for y in range(0, len(topo_map[0])):
            CurrPoint = topo_map[x][y]
            if CurrPoint.val == 0:
                results = []
                currPointAnswer= modifiedDFS(CurrPoint, results)
#                print(f'Trailhead{CurrPoint} has {len(currPointAnswer)} trail(s)')
                answer += len(currPointAnswer)

    return answer



if __name__ == "__main__":
    print(main())
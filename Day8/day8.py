FILEPATH = 'input.txt'


class Node():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def get_distance_to_another_node(self, otherNode):
        return (otherNode.x - self.x, otherNode.y - self.y)
    def is_same(self, otherNode):
        if self.x == otherNode.x and self.y == otherNode.y:
          return True



def create_clean_input(filepath):
    clean_input = []
    positions = {'#': []}
    with open(FILEPATH, 'r') as file:
        for x, line in enumerate(file):
            input_line = line
            for y, char in enumerate(line):
                if char.isalnum():
                    if char not in positions:
                        positions[char] = [Node(x, y)]
                    else:
                        positions[char].append(Node(x, y))
            clean_input.append([x for x in input_line.strip()])
    return (clean_input, positions)


data = create_clean_input(FILEPATH)
positions = data[1]
clean_input = data[0]


def create_antinodes(node1, allNodes, positions):
    new_antinodes = []
    for otherNode in allNodes:
        dist = node1.get_distance_to_another_node(otherNode)
        if dist == (0, 0):
            pass
        else:
            newNode1 = (node1.x-dist[0], node1.y-dist[1])
            newNode2 = (otherNode.x+dist[0], otherNode.y+dist[1])
            new_antinodes.extend([newNode1, newNode2])
    return new_antinodes 


def process_positions(positions):
    for key in positions:
        all_new_antinodes = []
        if len(positions[key]) > 1:
            for node in positions[key]:
                new_antinodes = create_antinodes(node, positions[key], positions)
                for node in new_antinodes:
                    if node not in all_new_antinodes:
                        all_new_antinodes.append(node)
        for xy_coords in all_new_antinodes:
            if xy_coords not in positions['#']:
                positions['#'].append(xy_coords)
    return positions


positions = process_positions(positions)


def remove_oob_antinodes(x_len, y_len, positions):
    list_to_remove = []
    for val in positions['#']:
        if val[0] >= x_len or val[0] < 0 or val[1] >= y_len or val[1] < 0:
            list_to_remove.append(val)
    for val in list_to_remove:
        positions['#'].remove(val)
    return positions

positions = remove_oob_antinodes(len(clean_input), len(clean_input[0]), positions)


print(positions)
print(len(positions['#']))

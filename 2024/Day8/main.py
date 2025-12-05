from dataclasses import dataclass
import itertools

@dataclass(frozen=True)
class Node:
    x : int
    y : int
    symbol : str

    def _get_nodes_in_line(self, distance, max_x, max_y):
        next_node_x = self.x + distance[0]
        next_node_y = self.y + distance[1]
        while 0 <= next_node_x < max_x and 0 <= next_node_y < max_y:
            yield Node(next_node_x, next_node_y, self.symbol)
            next_node_x += distance[0]
            next_node_y += distance[1]


def process_input(FILEPATH):
    clean_input = []
    positions = {'#': []}
    with open(FILEPATH, 'r') as file:
        for x, line in enumerate(file):
            input_line = line
            for y, char in enumerate(line):
                if char.isalnum():
                    if char not in positions:
                        positions[char] = [Node(x, y, char)]
                    else:
                        positions[char].append(Node(x, y, char))
            clean_input.append([x for x in input_line.strip()])
    max_x = len(clean_input)
    max_y = len(clean_input[0])
    return max_x, max_y, positions


def create_new_nodes_from_node(currentNode, other_nodes, max_x, max_y):
    new_nodes = set()
    for node in other_nodes:
        dist = (node.x - currentNode.x, node.y - currentNode.y)
        for new_node in currentNode._get_nodes_in_line(dist, max_x, max_y):
            new_nodes.add(new_node)
    print(new_nodes)
    return new_nodes


def main():
    FILEPATH = 'input.txt'
    max_x, max_y, antennas_map = process_input(FILEPATH)
    nodes = set()
    for antennas in antennas_map.values():
        print(antennas)
        for node1, node2 in itertools.combinations(antennas, 2):
            print(node1)
            print(node2)
            dist = (node2.x - node1.x, node2.y - node1.y)
            for new_node in node1._get_nodes_in_line(dist, max_x, max_y):
                nodes.add(new_node)
    answer = len(nodes)
    print(nodes)
    print(answer)

main()

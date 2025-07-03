class Node():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def get_inline_nodes(self, distance, max_x, max_y):
        next_node_x = self.x + distance[0]
        next_node_y = self.y + distance[1]
        print('Next Node X Y {} {}'.format(next_node_x, next_node_y))
        if next_node_x > max_x or next_node_y > max_y or next_node_x < 0 or next_node_y < 0:
            print('next_node is out of bounds (over max or under 0)')
            return []
        else:
            NewCurrNode = (next_node_x, next_node_y)
            print('Working on {}\nNext Current Node: {}'.format(self, NewCurrNode))
            NextNode = Node(next_node_x, next_node_y)
            next_nodes = NextNode.get_inline_nodes(distance, max_x, max_y)
            print('next_nodes {}'.format(next_nodes))
            print('NewCurrNode {}'.format(NewCurrNode))
            print('Adding the lists {}'.format([NewCurrNode] + next_nodes))
            return [NewCurrNode] + next_nodes


FILEPATH = 'input.txt'


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
    print('clean_input {}\npositions {}'.format(clean_input, positions))
    print(list(map(str, positions.values())))
    return (clean_input, positions)


def create_new_nodes_from_node(currentNode, other_nodes, max_x, max_y):
    '''
    currentNode = Node()
    other_nodes = list of Nodes() excluding currentNode
    '''
    new_nodes = []
    for node in other_nodes:
        dist = (node.x - currentNode.x, node.y - currentNode.y)
        print('\n\nWorking on line from {},{} to {},{}\ndist = {}'.format(currentNode.x, currentNode.y, node.x, node.y, dist))
        new_nodes = new_nodes + currentNode.get_inline_nodes(dist, max_x, max_y)
        print('Done on Node{} and state of new_nodes is: {}'.format(node, new_nodes))
    print('All new nodes for currNode {},{}: {}'.format(currentNode.x, currentNode.y, new_nodes))
    return new_nodes


def loop_over_node_type(list_of_nodes_from_dict, max_x, max_y):
    new_nodes_for_type = []
    for i, currPoint in enumerate(list_of_nodes_from_dict):
        print('on i: {}'.format(i))
        print(list(map(str, list_of_nodes_from_dict)))
        tempCopy = list_of_nodes_from_dict.copy()
        tempCopy.pop(i)
        for k, otherPoint in enumerate(tempCopy):
            print(list(map(str, tempCopy)))
            print('on k: {}'.format(k))
            if k > i:
                distance = (otherPoint.x - currPoint.x,
                            otherPoint.y - currPoint.y)
            elif k <= i:
                distance = (otherPoint.x + currPoint.x,
                            otherPoint.y + currPoint.y)
            else:
                print('breaking')
                break
            print('Distance {}'.format(distance))
            c = currPoint.get_inline_nodes(distance, max_x, max_y)
            print('here')
            new_nodes_for_type = new_nodes_for_type + c
#            print(list(map(str, c)))
    return new_nodes_for_type


def main():
    data = create_clean_input(FILEPATH)
    max_x, max_y = len(data[0]), len(data[0][0])
    antennas_map = data[1]
#    max_x = 6
#    max_y = 6
#    a = Node(0, 0)
#    b = Node(1, 2)
#    c = Node(2, 4)
#    dist = (b.x - a.x, b.y - a.y
#    c = a.get_inline_nodes(dist, max_x, max_y)
#    print(c)
#    result = loop_over_node_type([a, b, c], max_x, max_y)
    del (antennas_map['#'])
    result = []
    for antenna_char in antennas_map:
        print(antenna_char)
        for currNode in antennas_map[antenna_char]:
            other_nodes = [node for node in antennas_map[antenna_char] if (node.x != currNode.x and node.y != currNode.y)]
            result += create_new_nodes_from_node(currNode, other_nodes, max_x, max_y)
    print(result)
    print(len(result))

    print(max_x)
    print(max_y)
    answer_map = []
    for x in range(max_x):
        answer_map.append(['.' for j in range(max_y)])
    print(answer_map)
    count = 0
    for i in range(max_x):
        for k in range(max_y):
            if (i, k) in result:
                answer_map[i][k] = '#'
                count += 1
    print('\n\n') 
    for row in answer_map:
        print('{}\n'.format(row))
    print(count)

main()

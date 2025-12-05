OPPOSITES = {
    'up' : 'down',
    'down' : 'up',
    'left' : 'right',
    'right' : 'left'
}

class Plot:
    def __init__(self, x: int, y: int, val: str, neighbors: dict):
        self.x = x
        self.y = y
        self.val = val
        self.neighbors = neighbors

    def link_neighbors(self, neighbor_plot: 'Plot', direction: str):
        self.neighbors[direction] = neighbor_plot
        neighbor_plot.neighbors[OPPOSITES[direction]] = self
    
    def link_oob_neighbor(self, direction: str):
        self.neighbors[direction] = None
        

def link_neighbors(farm_map):
    len_farm_map = len(farm_map)
    len_x_farm_map = len(farm_map[0])

    for x in range(0, len_farm_map):
        for y in range(0, len_x_farm_map):
            CurrPlot = farm_map[x][y]

            if x == 0:
                CurrPlot.link_oob_neighbor('up')
            elif x > 0 and x < len_farm_map:
                CurrPlot.link_neighbors(farm_map[x-1][y], 'up')

            if x == len_farm_map - 1:
                CurrPlot.link_oob_neighbor('down')

            if y == 0:
               CurrPlot.link_oob_neighbor('left')
            elif y > 0 and y < len_x_farm_map:
                CurrPlot.link_neighbors(farm_map[x][y-1], 'left')

            if y == len_x_farm_map - 1:
                CurrPlot.link_oob_neighbor('right')
                
              
def find_group(CurrPlot: Plot, group: list, checked: set) -> list[Plot]:
   
    checked.add(CurrPlot)

    if CurrPlot not in group:
        group.append(CurrPlot)

    for NeighborPlot in CurrPlot.neighbors.values():
        if NeighborPlot is not None:
            if NeighborPlot.val == CurrPlot.val and NeighborPlot not in checked:
                new_plots = find_group(NeighborPlot, group, checked)
                if new_plots is not None:
                    group.extend([plot for plot in new_plots if plot not in group])
    return group


def get_fence_price_for_group(plot_group: list, CHECKED_PLOTS: set) -> int:
    edges = 0
    for plot in plot_group:
        CHECKED_PLOTS.add(plot)
        neighbors = plot.neighbors.values()
        for n in neighbors:
            if n is None:
                edges += 1
            elif n.val != plot.val:
                edges += 1
    plots_len = len(plot_group) 
    price = edges * plots_len
    return price


def main():
    filepath = 'input.txt'
    input_map = []
    with open(filepath, 'r') as file:
        for x, line in enumerate(file.readlines()):
            new_row = []
            for y, char in enumerate(line.strip()):
                new_row.append(Plot(x, y, char, {}))
            input_map.append(new_row)

    link_neighbors(input_map)
    
    CHECKED_PLOTS = set() 
    answer = 0

    for row in input_map:
        for TestPlot in row:
            if TestPlot not in CHECKED_PLOTS:
                plot_group = find_group(TestPlot, group=[], checked=set())
                price = get_fence_price_for_group(plot_group, CHECKED_PLOTS)
                answer += price

    print(answer) 
    return answer


if __name__ == '__main__':
    main()
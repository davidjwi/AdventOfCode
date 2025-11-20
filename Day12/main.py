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
                
              
def DFS(plot: Plot, group: list, checked: list) -> list[Plot]:
    if plot not in group:
        group.append(plot)
    if plot not in checked:
        checked.append(plot)
        work_on = []
        for NeighborPlot in plot.neighbors.values():
            if NeighborPlot is not None:
                if NeighborPlot.val == plot.val and NeighborPlot not in checked:
                    work_on.append(NeighborPlot)
        if len(work_on) == 0:
            return group
        else:
            plot_group = []
            for NeighborPlot in work_on:
                 new_plots = DFS(NeighborPlot, group, checked)
                 if new_plots is not None:
                     for x in new_plots:
                         if x not in plot_group:
                             plot_group.append(x)
            return plot_group
    

def main():
    filepath = 'input.txt'
    farm_map = []
    with open(filepath, 'r') as file:
        for x, line in enumerate(file.readlines()):
            new_row = []
            for y, char in enumerate(line.strip()):
                new_row.append(Plot(x, y, char, {}))
            farm_map.append(new_row)

    link_neighbors(farm_map)
    
    checked_plots = []
    distinct_plot_groups = []

    for row in farm_map:
        for test_plot in row:
            if test_plot not in checked_plots:
                plot_group = DFS(test_plot, group=[], checked=[])

                distinct_plot_groups.append(plot_group)
                checked_plots.extend(plot_group)

    answer = 0
    for p_group in distinct_plot_groups:
        edges = 0
        val = p_group[0].val
        checked_neighbors = []
        for plot in p_group:
            neighbors = plot.neighbors.values()
            for n in neighbors:
                if n is None:
                    edges += 1
                elif n.val != plot.val:
                    edges += 1
            checked_neighbors.append(plot)
        plots_len = len(p_group) 
        price = edges * plots_len
        answer += price
    print(answer)

    return None


if __name__ == '__main__':
    main()
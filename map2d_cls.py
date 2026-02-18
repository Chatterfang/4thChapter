"""
class to contain 2d array of Node objects

args:
    max_x (int): max number of columns
    max_y (int): max number of rows
returns:
    class instance
"""
class Map2d:
    def __init__(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        self.map_arr = []
        self.num_nodes = 0

    # fills the 2d map with Nodes containing both own and neighbour IDs
    def populate_array(self):
        for y in range(self.max_y):
            for x in range(self.max_x):
                self.map_arr.append(Node(x, y, self.num_nodes))
                self.map_arr[self.num_nodes].assign_neighbours(self.max_x, self.max_y)
                self.num_nodes += 1

    # terminal printout of the 2d map
    def print_map(self):
        print(f'---2D MAP VIEW---')
        for y in range(self.max_y):
            for x in range(self.max_x):
                id_num = str(y * self.max_x + x)
                print(f'[{id_num.center(3, " ")}]', end='')
            print('')



class Node:
    def __init__(self, x, y, id_num):
        self.x = x
        self.y = y
        self.id_num = id_num
        self.neighbours = [-1, -1, -1, -1]

    def assign_neighbours(self, max_x, max_y):
        # order of neighbours (index)
        # 0: up, 1: left, 2: down, 3: right
        # value: -1 if not existing, otherwise id_num
        if self.y-1 >= 0:    # up
            self.neighbours[0] = ((self.y-1)*max_x + self.x)
        if self.x-1 >= 0:    # left
            self.neighbours[1] = (self.y*max_x + (self.x-1))
        if self.y+1 < max_y:    # down
            self.neighbours[2] = ((self.y+1)*max_x + self.x)
        if self.x+1 < max_x:    # right
            self.neighbours[3] = (self.y*max_x + (self.x+1))



def test_main():
    tmp_map = Map2d(8,5)
    tmp_map.populate_array()
    tmp_map.print_map()

# run
test_main()

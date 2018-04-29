# author: YUHAO HE
# Student number: 301255434
# date: 2017.1.22

from Queue import PriorityQueue

# main function: accept user inputs
def main():

    # test case
    # gird size n = 5
    # start location = (1, 1)
    # goal location = (5, 3)
    # grid values = [[100, 99, 120, 30, 70], [3, 1, 110, 97, 68], [103, 2, 105, 89, 92], [87, 4, 2, 201, 73],
    # [110, 90, 5, 80, 81]]
    # -----------------------------------------
    # the grid:
    # 110  90  5    80  81
    # 87   4   2    201 73
    # 103  2   105  89  92
    # 3    1   110  97  68
    # 100  99  120  30  70
    # ------------------------------------------
    # the least cost path = [(1, 1), (2, 1), (2, 2), (3, 2), (4, 2), (4, 3), (5, 3)]
    # the least cost = 23
    least_cost_path = path_find(5, (1,1), (5,3), [[100,99,120,30,70], [3,1,110,97,68], [103,2,105,89,92], [87,4,2,201,73], [110,90,5,80,81]])
    print "the least-cost path is: ", least_cost_path

# find the least_cost_path
def path_find(size, start, goal, values):
    # queue holds all the frontier in the form: (sum_cost, [path])
    frontiers = PriorityQueue()
    # the list holds all the cells that have been visited
    cell_visited = []
    path = []
    sum_cost = 0
    # put the root into queue
    frontiers.put((sum_cost, [start]))

    # check if frontiers is empty
    while frontiers.empty() == False:

        # dequeue the frontier with the least cost
        frontier_expand = tuple(frontiers.get(-1))
        sum_cost = frontier_expand[0]
        # a list of tuples
        path = list(frontier_expand[1])
        # print "the path is: ", path
        # get the frontier on the path (a tuple)
        frontier_loc = path[-1]
        cell_visited.append(frontier_loc)
        # print "frontier to be expanded is: ", frontier_expand

        # if reaches to the goal location, print the path and exit
        if frontier_loc == goal:
            print "the least cost is: ", frontier_expand[0]
            return path
        # else we expand the frontier and get its neighbors
        else:
            row_index = frontier_loc[0]
            col_index = frontier_loc[1]
            # print "the row index is: ", row_index
            # print "the column index is: ", col_index
            # add its neighbors into frontiers
            # if cell is NOT on bottom edge
            if row_index != 1 and (row_index - 1, col_index) not in cell_visited:
                cost = sum_cost + values[row_index - 2][col_index - 1] + 1
                frontier_path = list(path)
                frontier_path.append((row_index - 1, col_index))
                frontier = (cost, frontier_path)
                frontiers.put(frontier)
            # if cell is NOT on left edge
            if col_index != 1 and (row_index, col_index - 1) not in cell_visited:
                cost = sum_cost + values[row_index - 1][col_index - 2] + 1
                frontier_path = list(path)
                frontier_path.append((row_index, col_index - 1))
                frontier = (cost, frontier_path)
                frontiers.put(frontier)
            # if cell is NOT on top edge
            if row_index != size and (row_index + 1, col_index) not in cell_visited:
                cost = sum_cost + values[row_index][col_index - 1] + 1
                frontier_path = list(path)
                frontier_path.append((row_index + 1, col_index))
                frontier = (cost, frontier_path)
                frontiers.put(frontier)
            # if cell is NOT on right edge
            if col_index != size and (row_index, col_index + 1) not in cell_visited:
                cost = sum_cost + values[row_index - 1][col_index] + 1
                frontier_path = list(path)
                frontier_path.append((row_index, col_index + 1))
                frontier = (cost, frontier_path)
                frontiers.put(frontier)

main()

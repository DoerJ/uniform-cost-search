# Uniform-cost search
Utilize uniform-cost search algorithm to determines the least cost path from the start location to goal location

## Course
<dt>2018 Spring, SFU</dt>
<dt>SFU CMPT 310: Artificial Intelligence Survey</dt>

## Author
James(Yuhao) He

## Description
The problem involves the path finding in a n*n square, where each cell contains a non-negative integer indicating the "cost" of being in that cell. The cost of move is: 1 + value of the cell to be moved to. Given the starting position and goal position on the grid, the goal is to determines the least cost path from the start location to goal location. 

## Sample inputs
<dt>grid:</dt>
<dt>1   4   5   3</dt>
<dt>2   1   4   2</dt>
<dt>5   7   9   1</dt>
<dt>2   4   1   5</dt>
</br>
<dt>starting location: (1,1)</dt>
<dt>goal location: (4,3)</dt>

## Output
The output is the optimal path from starting location to goal location. For example, optimal path = [(1,1), (1,2), ..., (4,3)]


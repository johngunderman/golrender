import bpy
import copy


iteration = [
    [1,0,1,1,0,0,0,1],
    [1,0,0,0,1,0,0,0],
    [0,0,0,1,0,1,0,1],
]


def draw_iteration(iteration, level):
    x_center = len(iteration) / 2.0
    y_center = len(iteration[0]) / 2.0
    for row in range(len(iteration)):
        for column in range(len(iteration[row])):
            if iteration[row][column] is 1:
                bpy.ops.mesh.primitive_cube_add(
                    location=[(row - x_center) * 2, (column - y_center) * 2, level])

def generate_next_iteration(current_iteration):
    new_iteration = copy.deepcopy(current_iteration)
    for row in range(len(current_iteration)):
        for column in range(len(current_iteration[row])):
            neighbor_count = get_neighbor_count(current_iteration, row, column)
        # Any live cell with fewer than two live neighbours dies, as if caused by under-population.
        if current_iteration[row][column] is 1 and neighbor_count < 2:
            new_iteration[row][column] = 0
            continue
        # Any live cell with two or three live neighbours lives on to the next generation.
        if current_iteration[row][column] is 1 and neighbor_count <= 3:
            continue
        # Any live cell with more than three live neighbours dies, as if by overcrowding.
        if current_iteration[row][column] is 1 and neighbor_count > 3:
            new_iteration[row][column] = 0
            continue
        if current_iteration[row][column] is 0 and neighbor_count is 3:
            new_iteration[row][column] = 1
        # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

def get_neighbor_count(iteration, row, column):
    return 0

draw_iteration(iteration, 0)


# exec(compile(open('/Users/johngunderman/src/golrender/render.py').read(), '/Users/johngunderman/src/golrender/render.py', 'exec'))

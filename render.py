import bpy
import copy


iteration = [
    [1,0,1,1,0,0],
    [1,0,0,0,1,0],
    [0,0,0,1,0,1],
    [1,0,1,1,0,0],
    [1,0,0,0,1,0],
    [0,0,0,1,0,1],
]


def draw_iteration(iteration, level):
    x_center = len(iteration) / 2.0
    y_center = len(iteration[0]) / 2.0
    m = 2.1
    for row in range(len(iteration)):
        for column in range(len(iteration[row])):
            if iteration[row][column] is 1:
                bpy.ops.mesh.primitive_cube_add(
                    location=[
                        (row - x_center) * m,
                        (column - y_center) * m,
                        level * m])

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
            # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
            if current_iteration[row][column] is 0 and neighbor_count is 3:
                new_iteration[row][column] = 1
    return new_iteration

def get_neighbor_count(iteration, row, column):
    count = 0
    max_row = len(iteration) - 2
    max_col = len(iteration[0]) - 2
    # D: D:
    if column  >= 1 and iteration[row][column - 1] is 1:
        count += 1
    if column <= max_col and iteration[row][column + 1] is 1:
        count += 1
    if row >= 1 and iteration[row - 1][column] is 1:
        count += 1
    if row <= max_row and iteration[row + 1][column] is 1:
        count += 1
    if row >= 1 and column >= 1 and iteration[row - 1][column - 1] is 1:
        count += 1
    if row <= max_row and column >= 1 and iteration[row + 1][column - 1] is 1:
        count += 1
    if row >= 1 and column <= max_col and iteration[row - 1][column + 1] is 1:
        count += 1
    if row <= max_row and column <= max_col and iteration[row + 1][column + 1] is 1:
        count += 1
    return count


def draw_generations(gen, iteration_count):
    for i in range(iteration_count):
        draw_iteration(gen, i)
        gen = generate_next_iteration(gen)

draw_generations(iteration, 5)

# exec(compile(open('/Users/johngunderman/src/golrender/render.py').read(), '/Users/johngunderman/src/golrender/render.py', 'exec'))

import bpy


iteration = [
    [1,0,1,1,0,0,0,1],
    [1,0,0,0,1,0,0,0],
    [0,0,0,1,0,1,0,1],
]


def draw_iteration(iteration, level):
    for row in range(len(iteration)):
        for column in range(len(iteration[row])):
            if iteration[row][column] is 1:
                bpy.ops.mesh.primitive_cube_add(location=[row * 2,column * 2,level])

draw_iteration(iteration, 0)


# exec(compile(open('/Users/johngunderman/src/golrender/render.py').read(), '/Users/johngunderman/src/golrender/render.py', 'exec'))

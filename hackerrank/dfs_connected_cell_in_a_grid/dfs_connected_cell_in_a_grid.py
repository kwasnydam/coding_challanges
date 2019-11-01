import os


def maxRegion(grid):
    seen = set()
    max_region = 0
    grid_width, grid_height = get_grid_dimensions(grid)
    for x in range(grid_height):
        for y in range(grid_width):
            start = (x, y)
            if decode(start) not in seen:
                current_region = region(grid, start, seen)
                if current_region > max_region:
                    max_region = current_region
    return max_region

def region(grid, coordinates, seen):
    if decode(coordinates) not in seen:
        seen.add(decode(coordinates))
    else:
        return 0
    x, y = coordinates
    current_val = grid[x][y]
    if current_val == 0:
        return 0
    else:
        to_visit = get_valid_neighbours(grid, coordinates, seen)
        return 1 + sum([region(grid, neighbour, seen) for neighbour in to_visit])

def decode(coordinates):
    return '{}{}'.format(coordinates[0], coordinates[1])

def get_valid_neighbours(grid, coordinates, seen):
    valid_neighbours = []
    x, y = coordinates
    for i in range(-1, 2):
        for j in range(-1, 2):
            if is_valid_neighbour(x, y, i, j, grid):
                valid_neighbours.append((x+i, y+j))
    return valid_neighbours

def is_valid_neighbour(x, y, i, j, grid):
    grid_width, grid_height = get_grid_dimensions(grid)
    x_i_coord_within_border = x + i >= 0 and x + i < grid_height
    y_i_coord_within_border = y + j >= 0 and y + j < grid_width
    i_j_not_both_zero = not [x + i, y + j] == [x, y]
    return x_i_coord_within_border and y_i_coord_within_border and i_j_not_both_zero

def get_grid_dimensions(grid):
    grid_width = len(grid[0])
    grid_height = len(grid)
    return grid_width, grid_height

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()

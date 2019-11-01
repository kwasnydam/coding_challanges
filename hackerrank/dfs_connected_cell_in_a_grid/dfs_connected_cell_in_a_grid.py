import os

def maxRegion(grid):
    seen = set()
    max_region = 0
    grid_width = len(grid[0])
    grid_height = len(grid)
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
        print('visiting node {}'.format(coordinates))
        seen.add(decode(coordinates))
    else:
        return 0
    x = coordinates[0]
    y = coordinates[1]
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
    grid_width = len(grid[0])
    grid_height = len(grid)
    x = coordinates[0]
    y = coordinates[1]
    for i in range(-1, 2):
        for j in range(-1, 2):
            # print(x+i, y+j)
            if x + i >= 0 and x + i < grid_height and y + j >= 0 and y + j < grid_width and not [x + i, y + j] == [x, y]:
                # print('appending {}'.format((x+i, y+j)))
                valid_neighbours.append((x+i, y+j))
    print('For coor = {} valid valid_neighbours = {}'.format(coordinates, valid_neighbours))
    return valid_neighbours

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

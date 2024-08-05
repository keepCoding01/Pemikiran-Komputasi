from collections import deque


def is_valid_move(grid, x, y):
    n = len(grid)
    m = len(grid[0])
    return 0 <= x < n and 0 <= y < m and grid[x][y] != '*'


def get_neighbors(grid, x, y):
    neighbors = []
    if is_valid_move(grid, x - 1, y):
        neighbors.append((x - 1, y))
    if is_valid_move(grid, x + 1, y):
        neighbors.append((x + 1, y))
    if is_valid_move(grid, x, y - 1):
        neighbors.append((x, y - 1))
    if is_valid_move(grid, x, y + 1):
        neighbors.append((x, y + 1))
    return neighbors


def find_min_direction_changes(grid, start_x, start_y, end_x, end_y):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # N, S, W, E
    visited = set()
    queue = deque([(start_x, start_y, None, 0)])  # (x, y, direction, changes)

    while queue:
        x, y, current_direction, changes = queue.popleft()

        if (x, y) == (end_x, end_y):
            return changes

        if (x, y, current_direction) not in visited:
            visited.add((x, y, current_direction))

            for d in directions:
                new_x, new_y = x + d[0], y + d[1]
                if is_valid_move(grid, new_x, new_y):
                    new_direction = d
                    if current_direction is None or current_direction == new_direction:
                        queue.append((new_x, new_y, new_direction, changes))
                    else:
                        queue.append(
                            (new_x, new_y, new_direction, changes + 1))

    return -1


def main():
    # Membaca input
    n, m = map(int, input().split())
    grid = []
    for i in range(n):
        grid.append(list(input()))

    # Menemukan posisi awal (V) dan akhir (H)
    start_x, start_y = None, None
    end_x, end_y = None, None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'V':
                start_x, start_y = i, j
            elif grid[i][j] == 'H':
                end_x, end_y = i, j

    # Mencari jalur dengan perubahan arah minimum
    min_direction_changes = find_min_direction_changes(
        grid, start_x, start_y, end_x, end_y)

    # Menampilkan hasil
    print(f"Jumlah minimum perubahan arah: {min_direction_changes}")


# Memulai program
main()

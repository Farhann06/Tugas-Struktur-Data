import time

ROWS = 5
COLS = 5

# Grid awal
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# Fungsi menampilkan grid
def print_grid(grid):
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                print("■", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

# Simulasi 5 generasi
for gen in range(5):
    print("Generasi:", gen)
    print_grid(grid)

    # Buat grid baru kosong
    new_grid = []
    for r in range(ROWS):
        new_grid.append([0] * COLS)

    # Hitung generasi berikutnya
    for r in range(ROWS):
        for c in range(COLS):

            # Hitung tetangga hidup
            neighbors = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    nr = r + i
                    nc = c + j
                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        neighbors += grid[nr][nc]

            # Aturan Game of Life
            if grid[r][c] == 1:
                if neighbors == 2 or neighbors == 3:
                    new_grid[r][c] = 1
            else:
                if neighbors == 3:
                    new_grid[r][c] = 1

    grid = new_grid
    time.sleep(1)

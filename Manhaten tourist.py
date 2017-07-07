__author__ = 'dongpei'

# Dynamic programming solution to the Manhattan Tourist Problem
# h = horizontal weights; h[i][j] = attractions between h[i][j-1] and h[i][j]
# v = vertical weights; v[i][j] = attractions between v[i-1][j] and v[i][j]
# rows and columns are the number of rows and columns in the grid
def ManhattanTourist(v, h, rows, columns):

    # Set up an empty rows x columns matrix.
    MT = []
    for r in range(0, rows):
        MT.append([0] * columns)

    # Fill in the first row and first column.
    MT[0][0] = 0
    for r in range(1, rows):
        MT[r][0] = MT[r - 1][0] + v[r][0]
    for c in range(1, columns):
        MT[0][c] = MT[0][c-1] + h[0][c]

    # Then fill in the rest of the table.
    for r in range(1, rows):
        for c in range(1, columns):
            MT[r][c] = max(MT[r-1][c] + v[r][c], MT[r][c-1] + h[r][c])

    return MT

v = [[0, 0, 0, 0], [1, 0, 2, 4], [4, 6, 5, 2], [4, 4, 5, 2]]
h = [[0, 3, 2, 4], [0, 3, 2, 4], [0, 0, 7, 3], [0, 3, 3, 1]]
print ManhattanTourist(v, h, 4, 4)

rows=4
columns=4

MT[0][0] = 0
for r in range(1, rows):
   MT[r][0] = MT[r - 1][0] + v[r][0]
for c in range(1, columns):
        MT[0][c] = MT[0][c-1] + h[0][c]


for r in range(1,4):
    print r
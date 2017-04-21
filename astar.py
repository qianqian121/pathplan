from random import randint

def board_print():
    for r in board:
        print r

n = 8
board = [[0 for i in range(n)] for j in range(n)]

# board_print()
# board[2][3] = 1
# board_print()

def obj_gen(num_obj=10):
    global board
    for i in range(num_obj):
        x = randint(0, n - 1)
        y = randint(0, n - 1)
        board[x][y] = 1
    board_print()

def astar(board):
    return

# obj_gen()

board = [[0, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0]]

# board_print()

q = []
trace = {}

def move(prev, x, y):
    global q
    global board
    global trace
    if x < 0 or x >= n or y < 0 or y >= n or board[x][y] != 0:
        return
    q.insert(0, (x, y))
    board[x][y] = 4
    trace[(x, y)] = prev

def bfs():
    # global board
    q.insert(0, (0, 0))
    board[0][0] = 4
    while q:
        cur = q.pop()
        x = cur[0]
        y = cur[1]
        if x == n-1 and y == n-1:
            break

        move((x, y), x-1, y-1)
        move((x, y), x-1, y)
        move((x, y), x-1, y+1)
        move((x, y), x, y-1)
        move((x, y), x, y+1)
        move((x, y), x+1, y-1)
        move((x, y), x+1, y)
        move((x, y), x+1, y+1)

bfs()
# board_print()

def trace_print():
    global board
    prev = trace[(n-1, n-1)]
    while prev:
        # print(prev)
        board[prev[0]][prev[1]] = 8
        prev = trace.get(prev, None)
    board_print()

trace_print()
print('done')
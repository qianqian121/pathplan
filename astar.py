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

# trace_print()

def cost_gen(max_cost=9):
    global board
    for i in range(n):
        for j in range(n):
            board[i][j] = randint(1, max_cost)
    board_print()

# cost_gen()

board = [
    [9, 6, 8, 8, 3, 3, 9, 1],
    [8, 9, 3, 1, 6, 3, 2, 4],
    [3, 5, 8, 9, 1, 3, 5, 4],
    [5, 6, 2, 4, 2, 2, 7, 4],
    [6, 6, 7, 1, 8, 5, 9, 8],
    [2, 8, 6, 1, 7, 8, 5, 5],
    [6, 4, 8, 6, 7, 2, 7, 7],
    [5, 1, 1, 6, 3, 2, 6, 7]
]

import heapq as hq

class minq():
    def __init__(self):
        self.pq = []

    def push(self, e):
        hq.heappush(self.pq, e)

    def get(self):
        return hq.heappop(self.pq)[1]

    def peek(self):
        return hq.nsmallest(1, self.pq)

    def empty(self):
        return not self.pq

def dijkstra(board):
    pq = minq()

    start = (0, 0)
    cost_so_far = {}
    cost_so_far[start] = 0
    trace[start] = None
    pq.push((0, start))

    def board_print(board):
        for r in board:
            print r

    def mov(current, next):
        x = next[0]
        y = next[1]
        if x < 0 or x >= n or y < 0 or y >= n:
            return
        new_cost = cost_so_far[current] + board[current[0]][current[1]]
        if next not in cost_so_far or new_cost < cost_so_far[next]:
            pq.push((new_cost, next))
            cost_so_far[next] = new_cost
            trace[next] = current

    def trace_print(board):
        prev = trace[(n - 1, n - 1)]
        while prev:
            print(prev)
            board[prev[0]][prev[1]] = 0
            prev = trace.get(prev, None)
        board_print(board)

    while not pq.empty():
        cur = pq.get()

        if cur == (n-1, n-1):
            break

        x = cur[0]
        y = cur[1]
        mov((x, y), (x - 1, y - 1))
        mov((x, y), (x - 1, y))
        mov((x, y), (x - 1, y + 1))
        mov((x, y), (x, y - 1))
        mov((x, y), (x, y + 1))
        mov((x, y), (x + 1, y - 1))
        mov((x, y), (x + 1, y))
        mov((x, y), (x + 1, y + 1))

    trace_print(board)

# dijkstra(board)

def greedy(board, start=(0,0), end=(n-1,n-1)):
    def heuristic(current, goal):
        return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

    def board_print(board):
        for r in board:
            print r

    def trace_print(board):
        prev = trace[(n - 1, n - 1)]
        while prev:
            print(prev)
            board[prev[0]][prev[1]] = 0
            prev = trace.get(prev, None)
        board_print(board)

    def mov(current, next):
        x = next[0]
        y = next[1]
        if x < 0 or x >= n or y < 0 or y >= n:
            return

        if next not in trace:
            priority = heuristic(next, end) + board[x][y]
            pq.push((priority, next))
            trace[next] = current

    pq = minq()
    trace = {}
    trace[start] = None
    pq.push((0, start))

    while not pq.empty():
        cur = pq.get()
        if cur == end:
            break
        x = cur[0]
        y = cur[1]
        mov((x, y), (x - 1, y - 1))
        mov((x, y), (x - 1, y))
        mov((x, y), (x - 1, y + 1))
        mov((x, y), (x, y - 1))
        mov((x, y), (x, y + 1))
        mov((x, y), (x + 1, y - 1))
        mov((x, y), (x + 1, y))
        mov((x, y), (x + 1, y + 1))

    trace_print(board)

greedy(board)
# print('done')

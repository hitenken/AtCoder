#迷路の最短距離を解く　ゴール:G

import queue

class pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getter(self):
        return [self.x, self.y]

def solvmaiz():
    N, M = map(int, input().split())
    maze = [[x for x in input().split()]for y in range(M)]
    #maze = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    q = queue.Queue()
    INF = 10**5
    d = [[INF for x in range(N)]for y in range(M)]
    q.put(pair(0,0))
    d[0][0] = 0
    goal = [0, 0]
    while(not q.empty()):
        p = q.get().getter()
        if maze[p[0]][p[1]] == 'G':
            goal[0] = p[0]
            goal[1] = p[1]
            break
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M and d[nx][ny] == INF:
                q.put(pair(nx,ny))
                d[nx][ny] = d[p[0]][p[1]] + 1

    return d[goal[0]][goal[1]]
if __name__ == "__main__":
    ans = solvmaiz()
    print(ans)
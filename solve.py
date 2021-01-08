import sys
from collections import deque
input = sys.stdin.readline
dy, dx = [0, 0, 1, -1, -1, -1, 1, 1], [1, -1, 0, 0, 1, -1, 1, -1]  # 동 서 남 북 북동 북서 남동 남서

def bfs(y,x):
    dq=deque()
    dq.append([y,x])
    while dq:
        y,x=dq.popleft()
        mapp[y][x]=0
        for i in range(8):
            ny,nx=y+dy[i], x+dx[i]
            if 0<=ny<n and 0<=nx<m and mapp[ny][nx]==1:
                dq.append([ny,nx])
while True:
    m,n=map(int, input().split())
    if n==0 and m==0:
        break
    mapp=[list(map(int, input().split())) for _ in range(n)]
    cnt=0
    for y in range(n):
        for x in range(m):
            if mapp[y][x]==1:
                cnt+=1
                bfs(y,x)
    print(cnt)
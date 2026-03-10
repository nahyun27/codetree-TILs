n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dp = [
    [0 for _ in range(n)] for _ in range(n)
]
dp[0][0] = grid[0][0]

def solve():
    for i in range(n):
        for j in range(n):
            if i >= 1 and j >= 1:
                tmp = max(dp[i][j-1], dp[i-1][j])
                return max(tmp, grid[i][j])
            if i >= 1: 
                return max(dp[i][j-1], grid[i][j])
            if j >= 1:
                return max(dp[i-1][j], grid[i][j])


print(solve())
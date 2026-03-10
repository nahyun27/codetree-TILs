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
                dp[i][j] = min(max(dp[i][j-1], grid[i][j]), max(dp[i-1][j], grid[i][j]))
            elif i > 0: 
                dp[i][j] = max(dp[i-1][j], grid[i][j])
            elif j > 0:
                dp[i][j] = max(dp[i][j-1], grid[i][j])
    return dp[n-1][n-1]


print(solve())

# print(dp)
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

def solve():
    cells = []  # (value, row, col)
    
    for i in range(N):
        row = grid[i]
        for j, v in enumerate(row):
            cells.append((v, i, j))
    
    # Step 1. 셀 값 기준 정렬
    cells.sort()
    sorted_vals = [c[0] for c in cells]
    
    ans = float('inf')
    
    # Step 2. 투 포인터
    l = 0
    for r in range(len(cells)):
        while l <= r:
            lo = sorted_vals[l]
            hi = sorted_vals[r]
            
            # Step 2-1. (0,0)과 (N-1,N-1)이 윈도우 안에 있는지 확인
            if not (lo <= grid[0][0] <= hi and lo <= grid[N-1][N-1] <= hi):
                break
            
            # Step 3. DP로 경로 존재 여부 확인
            def check(lo, hi):
                dp = [[False] * N for _ in range(N)]
                dp[0][0] = True
                for i in range(N):
                    for j in range(N):
                        if not (lo <= grid[i][j] <= hi):
                            continue
                        if i > 0 and dp[i-1][j]:
                            dp[i][j] = True
                        if j > 0 and dp[i][j-1]:
                            dp[i][j] = True
                return dp[N-1][N-1]
            
            if check(lo, hi):
                ans = min(ans, hi - lo)
                l += 1
            else:
                break
        
    print(ans)

solve()
#LEFT RIGHT UP DOWN

def nextMove(n,r,c,grid):
    for i in range(n):
        for j in range(n):
            if grid[i][j]=="p":
                if r>i:
                    return ("UP")
                elif r<i:
                    return ("DOWN")
                else:
                    if c>j:
                        return ("LEFT")
                    else:
                        return ("RIGHT")
                i=n
                break
    return ""

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
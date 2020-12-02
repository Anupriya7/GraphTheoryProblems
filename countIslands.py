r, c = 5, 5
mat = [
    [1, 1, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [1, 1, 0, 0, 1],
]

def isSafe(i, j, visited): 
    return (i >= 0 and i < r and 
            j >= 0 and j < c and 
            not visited[i][j] and mat[i][j]) 

def DFS(i, j, visited, lands): 
    rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1]
    colNbr = [-1,  0,  1, -1, 1, -1, 0, 1]
    visited[i][j] = True
    for k in range(8): 
        if isSafe(i + rowNbr[k], j + colNbr[k], visited): 
            lands.append(1)
            print(k,"lands",lands)
            print("i + rowNbr[k]",i+rowNbr[k])
            print("j+ colNbr[k]",j + colNbr[k])
            DFS(i + rowNbr[k], j + colNbr[k], visited, lands) 

    #print(lands)
    return lands

def countIslands(): 
    visited = [[False for j in range(c)]for i in range(r)] 
    count = 0
    allLands = []
    for i in range(r): 
        for j in range(c): 
            if visited[i][j] == False and mat[i][j] == 1: 
                temp = DFS(i, j, visited, [1]) 
                allLands.append(len(temp))
                print(allLands)
                count += 1
    return (max(allLands))

            

print(countIslands())



















# r, c = input().split()
# r, c = int(r), int(c)
# mat = []
# for i in range(r):
#     temp = input().split()
#     mat.append([int(i) for i in temp])


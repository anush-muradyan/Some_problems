import numpy as np 

def is_valid(mat,pos_x,pos_y):
    #left row
    for i in range(pos_y):
        if mat[pos_x][i]==1:
            return False
    #if 1 in mat[pos[0]]
        #return False
 
    #left upper diagonal
    for i,j in zip(range(pos_x,-1,-1),range(pos_y,-1,-1)):
        if mat[i][j] == 1:
            return False
    #left lower diagonal
    for i,j in zip(range(pos_x,len(mat),1),range(pos_y,-1,-1)):
        if mat[i][j] == 1:
            return False
    return True

def solve(mat,col=0):
    if col==len(mat):
        return True
    for row in range(n):
        if is_valid(mat, row, col):
            mat[row][col]=1
            if solve(mat, col + 1):
                return True
            mat[row][col] = 0
    return False

n = int(input("Enter n: "))
mat = np.zeros((n,n),dtype=int)

solve(mat)
print(mat)

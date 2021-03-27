def input_matrix(n):
    mat = []
    for _ in range(n):
        mat.append(input().split())
    return mat

def output_matrix(mat):
    n = len(mat)
    m = len(mat[0])
    for i in range(n):
        for j in range(m):
            print(mat[i][j],end = " ")
        print()

def find_B(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j]=="B":
                return i,j
    return -1,-1

def transform_diagonal(mat,direction,B_pos):
    x = direction[0]     #row
    y = direction[1]     #column
    n = len(mat)
    while 0 <= B_pos[0] + x < n and 0 <= B_pos[1] + y < n:
        mat[B_pos[0] + x][B_pos[1] + y] = "x"
        B_pos = B_pos[0] + x, B_pos[1] + y 

n = 8
mat = input_matrix(n)
#mat = [['.','.','.','.','.','.','.','.'],
#       ['.','.','.','.','.','.','.','.'],
#       ['.','.','.','.','.','.','.','.'],
#       ['.','.','B','.','.','.','.','.'],
#       ['.','.','.','.','.','.','.','.'],
#       ['.','.','.','.','.','.','.','.'],
#       ['.','.','.','.','.','.','.','.'],
#       ['.','.','.','.','.','.','.','.']]

position = find_B(mat)

dirs = [(1,1),(-1,-1),(1,-1),(-1,1)]
for d in dirs:
    transform_diagonal(mat,d,position)

print("*"*80)
output_matrix(mat)
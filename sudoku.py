def input_matrix(n=9):
    mat = []
    for _ in range(n):
        mat.append([int(elem) if elem!="." else elem for elem in input().split()])
    return mat

def output_matrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j],end=" ")
        print()

def find_empty(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]==".":
                return i,j

def is_valid(mat,num,pos_x,pos_y):
    #check rows
    for j in range(len(mat)):
        if mat[pos_x][j]==num:
            return False 

    #check columns
    for i in range(len(mat)):
        if mat[i][pos_y]==num:
            return False

    #check box
    box_x = pos_x // 3 * 3
    box_y = pos_y // 3 * 3
    for i in range(box_x,box_x+3):
        for j in range(box_y,box_y+3):
            if mat[i][j]==num:
                return False
    return True

def solve(mat):
    position = find_empty(mat)
    if not position:
        return True
    i,j = position
    for num in range(1,10):
        if is_valid(mat,num,i,j):
            mat[i][j]=num
            if solve(mat):
                return True
            mat[i][j]="."
    return False

board = [
    [7,8,'.',4,'.','.',1,2,'.'],
    [6,'.','.','.',7,5,'.','.',9],
    ['.','.','.',6,'.',1,'.',7,8],
    ['.','.',7,'.',4,'.',2,6,'.'],
    ['.','.',1,'.',5,'.',9,3,'.'],
    [9,'.',4,'.',6,'.','.','.',5],
    ['.',7,'.',3,'.','.','.',1,2],
    [1,2,'.','.','.',7,4,'.','.'],
    ['.',4,9,2,'.',6,'.','.',7]
]

solve(board)
print(board)

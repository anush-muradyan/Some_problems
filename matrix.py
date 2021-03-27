def input_matrix(n,m):
    mat = []
    for _ in range(n):
        row = [int(elem) for elem in input().split()]
        if len(row)!=m:
            print("Wrong input!!!")
            return
        mat.append(row)
    return mat

def output_matrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j],end = " ")
        print()

mat=input_matrix(3,2)
output_matrix(mat)

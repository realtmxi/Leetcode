# 数灵元科技面试
# Python 顺时针旋转打印二维数组

def rotate_print(matrix):
    rlt = []
    while matrix:
        rlt += matrix.pop(0) # adding the first row
        if matrix and matrix[0]:
            for row in matrix:
                rlt.append(row.pop())
        if matrix:
            rlt += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                rlt.append(row.pop(0))

    return rlt



if __name__=="__main__":
    matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    print(rotate_print(matrix))

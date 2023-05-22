# 数灵元科技面试
# Python 顺时针旋转打印二维数组

# solution 1
def rotate_print_1(matrix):
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


# solution 2
class Solution2:
    def printMatrix(self, matrix):
        rlt = []
        while(matrix):
            result += matrix.pop(0)
            if not matrix or not matrix[0]:
                break
            matrix = self.rotate(matrix)
        return rlt

    def rotate(self, matrix):
        row_len = len(matrix)
        col_len = len(matrix[0])
        newmat = []
        for i in range(col_len):
            newmat2 = []
            for j in range(row_len):
                newmat2.append(matrix[j][i])
            newmat.append(newmat2)
        newmat.reverse()
        return newmat
    

if __name__=="__main__":
    matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    print(rotate_print(matrix))
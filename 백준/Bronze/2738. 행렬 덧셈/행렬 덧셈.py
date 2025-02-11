n,m = map(int, input().split())

# 행렬 입력 함수
def input_matrix(n, m):
    return [list(map(int, input().split())) for _ in range(n)]

A = input_matrix(n, m)
B = input_matrix(n, m)

# 행렬 덧셈 함수
def add(matrix1, matrix2):
    return [[matrix1[i][j]+matrix2[i][j]for j in range(m)] for i in range(n)]
result = add(A, B)

for row in result:
    print(*row)
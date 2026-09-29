def transpose(mat):
    n = []
    if len(mat) > 0:
        ln = len(mat[0])
        for x in mat:
            if len(x) != ln:
                raise ValueError("Ошибка: рваная матрица")
        for x in range(ln):
            new_mat = []
            for y in mat:
                new_mat.append(y[x])
            n.append(new_mat)
    return n

def row_sums(mat):
    n = []
    ln = len(mat[0])
    for x in mat:
        if len(x) != ln:
            raise ValueError("Ошибка: рваная матрица")
        n.append(sum(x))
    return n

def col_sums(mat):
    n = []
    mat = transpose(mat)
    ln = len(mat[0])
    for x in mat:
        if len(x) != ln:
            raise ValueError("Ошибка: рваная матрица")
        n.append(sum(x))
    return n

# print("transpose")
# print(f"{[[1,2,3]]} -> {transpose([[1,2,3]])}")
# print(f"{[[1],[2],[3]]} -> {transpose([[1],[2],[3]])}")
# print(f"{[[1,2],[3,4]]} -> {transpose([[1,2],[3,4]])}")
# print(f"{[]} -> {transpose([])}")
# print(f"{[[1,2],[3]]} -> {transpose([[1,2],[3]])}")

# print("row_sums")
# print(f"{[[1,2,3],[4,5,6]]} -> {row_sums([[1,2,3],[4,5,6]])}")
# print(f"{[[-1,1],[10,-10]]} -> {row_sums([[-1,1],[10,-10]])}")
# print(f"{[[0,0],[0,0]]} -> {row_sums([[0,0],[0,0]])}")
# print(f"{[[1,2],[3]]} -> {row_sums([[1,2],[3]])}")

print("col_sums")
print(f"{[[1,2,3],[4,5,6]]} -> {col_sums([[1,2,3],[4,5,6]])}")
print(f"{[[-1,1],[10,-10]]} -> {col_sums([[-1,1],[10,-10]])}")
print(f"{[[0,0],[0,0]]} -> {col_sums([[0,0],[0,0]])}")
print(f"{[[1,2],[3]]} -> {col_sums([[1,2],[3]])}")
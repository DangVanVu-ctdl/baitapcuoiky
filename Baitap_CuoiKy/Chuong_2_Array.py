def DoiXung(matrix):
    n = len(matrix)
    
    # Kiểm tra kích thước của ma trận
    if n == 0:
        return True  # Ma trận rỗng được coi là đối xứng
    
    # Kiểm tra xem ma trận có vuông không
    if len(matrix[0]) != n:
        return False  # Không phải ma trận vuông
    
    # Kiểm tra từng phần tử của ma trận
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False  # Nếu phần tử không đối xứng thì trả về False
    return True  # Nếu tất cả các phần tử đều đối xứng thì trả về True

# Ví dụ sử dụng:
matrix1 = [[1, 5, 3],
           [2, 4, 5],
           [3, 5, 6]]

matrix2 = [[1, 2, 3],
           [2, 4, 2],
           [3, 2, 1]]

# Kiểm tra ma trận 1
print("Ma trận 1 có là ma trận đối xứng không?", DoiXung(matrix1))

# Kiểm tra ma trận 2
print("Ma trận 2 có là ma trận đối xứng không?", DoiXung(matrix2))

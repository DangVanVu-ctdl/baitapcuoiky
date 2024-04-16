### Câu 1:

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





### Câu 2:
def TamGiacTren(matrix):
    n = len(matrix)
    
    # Kiểm tra kích thước của ma trận
    if n == 0:
        return True  # Ma trận rỗng được coi là tam giác trên
    
    # Kiểm tra xem ma trận có vuông không
    if len(matrix[0]) != n:
        return False  # Không phải ma trận vuông
    
    # Kiểm tra từng phần tử của ma trận
    for i in range(n):
        for j in range(i + 1, n):  # Chỉ cần kiểm tra phần tử phía dưới đường chéo chính
            if matrix[i][j] != 0:
                return False  # Nếu có phần tử khác không ở phía dưới đường chéo chính thì không phải tam giác trên
    return True  # Nếu tất cả các phần tử phía dưới đường chéo chính đều bằng 0 thì là tam giác trên

# Ví dụ sử dụng:
matrix1 = [[1, 2, 3],
           [0, 4, 5],
           [0, 0, 6]]

matrix2 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

# Kiểm tra ma trận 1
print("Ma trận 1 có là ma trận tam giác trên không?", TamGiacTren(matrix1))

# Kiểm tra ma trận 2
print("Ma trận 2 có là ma trận tam giác trên không?", TamGiacTren(matrix2))





### Câu 3:
def TrungHang(matrix):
    n = len(matrix)
    
    # Kiểm tra kích thước của ma trận
    if n == 0:
        return False  # Ma trận rỗng không thể có hai hàng giống nhau
    
    # Kiểm tra từng cặp hàng
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i] == matrix[j]:
                return True  # Nếu có hai hàng giống nhau thì trả về True
    return False  # Nếu không có hai hàng giống nhau thì trả về False

# Ví dụ sử dụng:
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[1, 2, 3],
           [4, 5, 6],
           [1, 2, 3]]  # Có hai hàng giống nhau

# Kiểm tra ma trận 1
print("Ma trận 1 có ít nhất hai hàng giống nhau không?", TrungHang(matrix1))

# Kiểm tra ma trận 2
print("Ma trận 2 có ít nhất hai hàng giống nhau không?", TrungHang(matrix2))





## Câu 4:
def NhomHang(matrix):
    n = len(matrix)
    
    # Khởi tạo một từ điển để lưu trữ các nhóm chỉ mục hàng
    groups = {}
    
    # Tìm và lưu trữ các nhóm chỉ mục hàng của các hàng giống nhau
    for i in range(n):
        row = tuple(matrix[i])  # Chuyển hàng thành một tuple để có thể sử dụng làm khóa trong từ điển
        if row in groups:
            groups[row].append(i)  # Nếu hàng đã tồn tại trong từ điển thì thêm chỉ mục hàng vào nhóm
        else:
            groups[row] = [i]  # Nếu hàng chưa tồn tại trong từ điển thì tạo một nhóm mới
    
    # In ra các nhóm chỉ mục hàng
    for group in groups.values():
        print("Nhóm chỉ mục hàng:", ", ".join(str(x) for x in group))

# Ví dụ sử dụng:
matrix = [[1, 2, 3],
          [4, 5, 6],
          [1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [1, 2, 3]]  # Có hai nhóm hàng giống nhau: [0, 2, 5] và [1, 3]

# In ra các nhóm chỉ mục hàng của các hàng giống nhau
NhomHang(matrix)





### Câu 5:
def Cong(a, b):
    # Lấy độ dài của hai mảng
    len_a = len(a)
    len_b = len(b)
    
    # Tính độ dài của mảng kết quả
    max_len = max(len_a, len_b)
    result = [-1] * (max_len + 1)  # Khởi tạo mảng kết quả với tất cả phần tử là -1
    
    # Biến nhớ
    carry = 0
    
    # Thực hiện phép cộng từ phải sang trái
    for i in range(max_len - 1, -1, -1):
        sum_ab = carry  # Khởi tạo tổng bằng giá trị của biến nhớ
        if i >= max_len - len_a:
            sum_ab += int(a[i - (max_len - len_a)])  # Cộng giá trị của phần tử a nếu còn phần tử
        if i >= max_len - len_b:
            sum_ab += int(b[i - (max_len - len_b)])  # Cộng giá trị của phần tử b nếu còn phần tử
        
        # Cập nhật kết quả và biến nhớ
        result[i + 1] = sum_ab % 10
        carry = sum_ab // 10
    
    # Kiểm tra xem có tràn không
    if carry == 0:
        result.pop(0)  # Loại bỏ phần tử đầu nếu không có tràn
    else:
        result = [-1] * (max_len + 1)  # Khởi tạo mảng kết quả với tất cả phần tử là -1 nếu có tràn
    
    return result

# Ví dụ sử dụng:
a = [1, 2, 3]  # 123
b = [4, 5, 6]  # 456

# Thực hiện phép cộng
result = Cong(a, b)

# In ra kết quả
if result[0] == -1:
    print("Kết quả bị tràn")
else:
    print("Kết quả:", ''.join(str(x) for x in result))





### Câu 6:
def Tru(a, b):
    # Lấy độ dài của hai mảng
    len_a = len(a)
    len_b = len(b)
    
    # Tính độ dài của mảng kết quả
    max_len = len_a
    result = [-1] * max_len  # Khởi tạo mảng kết quả với tất cả phần tử là -1
    
    # Biến nhớ
    borrow = 0
    
    # Thực hiện phép trừ từ phải sang trái
    for i in range(max_len - 1, -1, -1):
        diff_ab = borrow  # Khởi tạo hiệu bằng giá trị của biến nhớ
        if i >= max_len - len_b:
            diff_ab += int(b[i - (max_len - len_b)])  # Trừ giá trị của phần tử b nếu còn phần tử
        
        # Trừ giá trị của phần tử a
        diff_ab = int(a[i]) - diff_ab
        
        # Kiểm tra nếu có mượn
        if diff_ab < 0:
            diff_ab += 10
            borrow = 1
        else:
            borrow = 0
        
        # Cập nhật kết quả
        result[i] = diff_ab
    
    return result

# Ví dụ sử dụng:
a = [3, 2, 1]  # 321
b = [1, 1]     #  11

# Thực hiện phép trừ
result = Tru(a, b)

# In ra kết quả
print("Kết quả:", ''.join(str(x) for x in result))





### Câu 7:
def Nhan(a, b):
    # Lấy độ dài của hai mảng
    len_a = len(a)
    len_b = len(b)
    
    # Tạo mảng kết quả với độ dài là tổng độ dài của hai mảng
    max_len = len_a + len_b
    result = [-1] * max_len
    
    # Thực hiện phép nhân từ phải sang trái
    for i in range(len_a - 1, -1, -1):
        for j in range(len_b - 1, -1, -1):
            mul_ab = int(a[i]) * int(b[j])  # Tính tích của các chữ số
            
            # Cập nhật vào mảng kết quả
            result[i + j + 1] = mul_ab % 10  # Lưu chữ số hàng đơn vị
            carry = mul_ab // 10  # Lưu chữ số hàng chục
            
            # Cộng chữ số hàng chục vào chữ số ở vị trí trước đó trong mảng kết quả
            k = i + j
            while carry > 0:
                mul_ab = result[k] + carry
                result[k] = mul_ab % 10
                carry = mul_ab // 10
                k -= 1
    
    # Kiểm tra xem có tràn không
    if result[0] == 0:
        result.pop(0)  # Loại bỏ các số 0 đầu tiên nếu có
    else:
        result = [-1] * max_len  # Khởi tạo mảng kết quả với tất cả phần tử là -1 nếu có tràn
    
    return result

# Ví dụ sử dụng:
a = [1, 2, 3]  # 123
b = [4, 5, 6]  # 456

# Thực hiện phép nhân
result = Nhan(a, b)

# In ra kết quả
if result[0] == -1:
    print("Kết quả bị tràn")
else:
    print("Kết quả:", ''.join(str(x) for x in result))





### Câu 8:
def TamGiacDuoi(matrix):
    n = len(matrix)
    
    # Kiểm tra kích thước của ma trận
    if n == 0:
        return False  # Ma trận rỗng không thể là tam giác dưới
    
    # Kiểm tra xem ma trận có vuông không
    if len(matrix[0]) != n:
        return False  # Không phải ma trận vuông
    
    # Kiểm tra từng phần tử của ma trận
    for i in range(n):
        for j in range(0, i):  # Chỉ cần kiểm tra phần tử phía trên đường chéo chính
            if matrix[i][j] != 0:
                return False  # Nếu có phần tử khác không ở phía trên đường chéo chính thì không phải tam giác dưới
    return True  # Nếu tất cả các phần tử phía trên đường chéo chính đều bằng 0 thì là tam giác dưới

# Ví dụ sử dụng:
matrix1 = [[1, 0, 0],
           [2, 3, 0],
           [4, 5, 6]]

matrix2 = [[1, 0, 0],
           [2, 3, 4],
           [0, 5, 6]]  # Ma trận tam giác dưới

# Kiểm tra ma trận 1
print("Ma trận 1 có là ma trận tam giác dưới không?", TamGiacDuoi(matrix1))

# Kiểm tra ma trận 2
print("Ma trận 2 có là ma trận tam giác dưới không?", TamGiacDuoi(matrix2))





### Câu 9:
def Tru(a, b):
    # Lấy phần dấu của a và b
    sign_a = a[0]
    sign_b = b[0]
    
    # Lấy phần số của a và b
    num_a = a[1:]
    num_b = b[1:]
    
    # Xác định phần số lớn hơn và phần số nhỏ hơn
    larger = num_a
    smaller = num_b
    if len(num_b) > len(num_a) or (len(num_b) == len(num_a) and num_b > num_a):
        larger = num_b
        smaller = num_a
    
    # Nếu hai số có dấu khác nhau, thực hiện phép cộng với số có dấu là 1
    if sign_a != sign_b:
        return Cong([1] + larger, smaller)
    
    # Nếu hai số có cùng dấu, thực hiện phép trừ bình thường
    return TruUtil(sign_a, larger, smaller)

def TruUtil(sign, larger, smaller):
    # Tạo mảng kết quả với độ dài bằng phần số của số lớn hơn
    result = [-1] * len(larger)
    
    # Biến nhớ
    borrow = 0
    
    # Thực hiện phép trừ từ phải sang trái
    for i in range(len(larger) - 1, -1, -1):
        diff_ab = borrow  # Khởi tạo hiệu bằng giá trị của biến nhớ
        if i >= len(larger) - len(smaller):
            diff_ab += int(smaller[i - (len(larger) - len(smaller))])  # Trừ giá trị của phần tử smaller nếu còn phần tử
        
        # Trừ giá trị của phần tử larger
        diff_ab = int(larger[i]) - diff_ab
        
        # Kiểm tra nếu có mượn
        if diff_ab < 0:
            diff_ab += 10
            borrow = 1
        else:
            borrow = 0
        
        # Cập nhật kết quả
        result[i] = diff_ab
    
    # Loại bỏ các số 0 đầu tiên nếu có
    while len(result) > 1 and result[0] == 0:
        result.pop(0)
    
    # Thêm phần dấu vào kết quả
    return [sign] + result

def Cong(a, b):
    # Lấy phần dấu của a và b
    sign_a = a[0]
    sign_b = b[0]
    
    # Lấy phần số của a và b
    num_a = a[1:]
    num_b = b[1:]
    
    # Nếu hai số có dấu khác nhau, thực hiện phép trừ với số có dấu là 0
    if sign_a != sign_b:
        return TruUtil(0, num_a, num_b)
    
    # Nếu hai số có cùng dấu, thực hiện phép cộng bình thường
    return CongUtil(num_a, num_b)

def CongUtil(a, b):
    # Tạo mảng kết quả với độ dài bằng số lớn hơn cộng thêm 1 vị trí cho biến nhớ
    result = [-1] * (max(len(a), len(b)) + 1)
    
    # Biến nhớ
    carry = 0
    
    # Thực hiện phép cộng từ phải sang trái
    for i in range(len(result) - 1, -1, -1):
        sum_ab = carry  # Khởi tạo tổng bằng giá trị của biến nhớ
        if i >= len(result) - len(a):
            sum_ab += int(a[i - (len(result) - len(a))])  # Cộng giá trị của phần tử a nếu còn phần tử
        if i >= len(result) - len(b):
            sum_ab += int(b[i - (len(result) - len(b))])  # Cộng giá trị của phần tử b nếu còn phần tử
        
        # Cập nhật kết quả và biến nhớ
        result[i] = sum_ab % 10
        carry = sum_ab // 10
    
    # Loại bỏ các số 0 đầu tiên nếu có
    while len(result) > 1 and result[0] == 0:
        result.pop(0)
    
    # Thêm phần dấu vào kết quả
    return [0] + result

# Ví dụ sử dụng:
a = [0, 1, 2, 3]  # 123
b = [1, 1, 0]     # -110

# Thực hiện phép trừ
result = Tru(a, b)

# In ra kết quả
if result[0] == -1:
    print("Kết quả bị tràn")
else:
    print("Kết quả:", ''.join(str(x) for x in result))





### Câu 10:
def DayConDaiNhat(a, b):
    # Tạo một ma trận lưu độ dài của dãy con chung
    m = len(a)
    n = len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Tìm dãy con chung và lưu vào ma trận dp
    max_length = 0
    end_index = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i
    
    # Tạo mảng kết quả từ ma trận dp
    result = a[end_index - max_length: end_index]
    
    return result

# Ví dụ sử dụng:
a = [1, 6, 2, 5, 3, 7, 9, 4, 2, 8, 1, 5]
b = [6, 2, 5, 3, 7, 9, 8, 1, 5]

# Tìm dãy con có độ dài lớn nhất trong cả hai mảng a và b
result = DayConDaiNhat(a, b)

# In ra kết quả
print("Dãy con có độ dài lớn nhất trong cả hai mảng a và b:", result)

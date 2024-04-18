### bài 1

def LienThong(dt):
    # Khởi tạo một tập hợp chứa tất cả các đỉnh đã được duyệt
    da_duyet = set()

    # Hàm đệ qui để duyệt đồ thị từ một đỉnh
    def dfs(dinh):
        # Đánh dấu đỉnh này là đã duyệt
        da_duyet.add(dinh)
        # Duyệt qua tất cả các đỉnh kề của đỉnh hiện tại
        for ke in dt[dinh]:
            # Nếu đỉnh kề chưa được duyệt thì tiến hành duyệt đỉnh kề đó
            if ke not in da_duyet:
                dfs(ke)

    # Chọn một đỉnh bất kỳ để bắt đầu duyệt đồ thị
    dinh_bat_dau = next(iter(dt.keys()))
    # Duyệt đồ thị từ đỉnh bắt đầu
    dfs(dinh_bat_dau)

    # Kiểm tra xem tất cả các đỉnh đã được duyệt chưa
    return len(da_duyet) == len(dt)

# Ví dụ sử dụng:
dt = {
    1: [2],
    2: [1, 3],
    3: [2, 4],
    4: [3]
}
print("Đồ thị là đồ thị liên thông?", LienThong(dt))





### bài 2
def SoThanhPhan(dt):
    # Khởi tạo một tập hợp chứa tất cả các đỉnh đã được duyệt
    da_duyet = set()
    # Khởi tạo biến đếm số thành phần liên thông
    so_thanh_phan = 0

    # Hàm đệ qui để duyệt đồ thị từ một đỉnh
    def dfs(dinh):
        # Đánh dấu đỉnh này là đã duyệt
        da_duyet.add(dinh)
        # Duyệt qua tất cả các đỉnh kề của đỉnh hiện tại
        for ke in dt[dinh]:
            # Nếu đỉnh kề chưa được duyệt thì tiến hành duyệt đỉnh kề đó
            if ke not in da_duyet:
                dfs(ke)

    # Duyệt qua tất cả các đỉnh của đồ thị
    for dinh in dt.keys():
        # Nếu đỉnh chưa được duyệt, tăng biến đếm số thành phần liên thông lên 1
        if dinh not in da_duyet:
            so_thanh_phan += 1
            # Duyệt đồ thị từ đỉnh này
            dfs(dinh)

    return so_thanh_phan

# Ví dụ sử dụng:
dt = {
    1: [2],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [6],
    6: [5]
}
print("Số thành phần liên thông của đồ thị:", SoThanhPhan(dt))





### bài 3
def ChuTrinh(dt):
    # Khởi tạo một tập hợp chứa tất cả các đỉnh đã được duyệt
    da_duyet = set()
    # Khởi tạo một tập hợp chứa các đỉnh đang được duyệt trong quá trình tìm chu trình
    dang_duyet = set()

    # Hàm đệ qui để kiểm tra chu trình bắt đầu từ một đỉnh
    def dfs(dinh):
        # Đánh dấu đỉnh hiện tại là đang được duyệt
        dang_duyet.add(dinh)
        # Duyệt qua tất cả các đỉnh kề của đỉnh hiện tại
        for ke in dt[dinh]:
            # Nếu đỉnh kề đã được duyệt và không phải là đỉnh cha của đỉnh hiện tại thì có chu trình
            if ke in dang_duyet and ke != dinh:
                return True
            # Nếu đỉnh kề chưa được duyệt, tiến hành duyệt đỉnh kề đó
            elif ke not in da_duyet:
                # Nếu từ đỉnh kề này có chu trình, trả về True
                if dfs(ke):
                    return True
        # Đánh dấu đỉnh hiện tại là đã duyệt xong
        da_duyet.add(dinh)
        # Loại bỏ đỉnh hiện tại khỏi danh sách đang duyệt
        dang_duyet.remove(dinh)
        return False

    # Duyệt qua tất cả các đỉnh của đồ thị
    for dinh in dt.keys():
        if dinh not in da_duyet:
            if dfs(dinh):
                return True

    return False

# Ví dụ sử dụng:
dt1 = {1: [2], 2: [3], 3: [4], 4: [2]}  # Có chu trình: 2 -> 3 -> 4 -> 2
print("Có chu trình:", ChuTrinh(dt1))  # Kết quả mong đợi: True

dt2 = {1: [2, 3], 2: [3], 3: [4], 4: []}  # Không có chu trình
print("Có chu trình:", ChuTrinh(dt2))  # Kết quả mong đợi: False





### bài 4
def ChuaDinh(dt, v):
    for dinh in dt.keys():
        if dinh == v:
            return True
    return False

# Ví dụ sử dụng:
dt = {1: [2, 3], 2: [3], 3: [4], 4: []}
print("Đỉnh 3 có trong đồ thị:", ChuaDinh(dt, 3))  # Kết quả mong đợi: True
print("Đỉnh 5 có trong đồ thị:", ChuaDinh(dt, 5))  # Kết quả mong đợi: False





### Bài 5
def BacDinh(dt, v):
    bac = 0
    
    # Duyệt qua các đỉnh kề của đỉnh v
    for neighbor in dt[v]:
        # Tăng bậc lên 1 cho mỗi đỉnh kề
        bac += 1
    
    return bac

# Ví dụ sử dụng
dt = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

dinh = 'B'
print("Bậc của đỉnh", dinh, "là:", BacDinh(dt, dinh))





### Bài 6
def SoCungVao(dt, v):
    # Khởi tạo số cung đi vào ban đầu là 0
    socung_vao = 0
    
    # Duyệt qua tất cả các đỉnh trong đồ thị
    for vertex in dt:
        # Kiểm tra xem đỉnh vertex có kề với đỉnh v không
        if v in dt[vertex]:
            # Nếu có, tăng số cung đi vào lên 1
            socung_vao += 1
    
    return socung_vao

# Ví dụ sử dụng
dt = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['A'],
    'D': ['A', 'C']
}

dinh = 'C'
print("Số cung đi vào đỉnh", dinh, "là:", SoCungVao(dt, dinh))





### Bài 7
def SoCungRa(dt, v):
    # Khởi tạo số cung đi ra ban đầu là 0
    socung_ra = 0
    
    # Kiểm tra số cung đi ra khỏi đỉnh v
    if v in dt:
        socung_ra = len(dt[v])
    
    return socung_ra

# Ví dụ sử dụng
dt = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['A'],
    'D': ['A', 'C']
}

dinh = 'B'
print("Số cung đi ra khỏi đỉnh", dinh, "là:", SoCungRa(dt, dinh))





### Bài 8
def DuongDi(dt, v1, v2):
    # Sử dụng DFS (Duyệt theo chiều sâu) để kiểm tra đường đi từ v1 đến v2
    def dfs(current_vertex, target_vertex, visited):
        # Đánh dấu đỉnh hiện tại đã được thăm
        visited.add(current_vertex)
        
        # Nếu đỉnh hiện tại là đỉnh đích, trả về True
        if current_vertex == target_vertex:
            return True
        
        # Duyệt qua các đỉnh kề của đỉnh hiện tại
        for neighbor in dt[current_vertex]:
            # Nếu đỉnh kề chưa được thăm, tiến hành DFS từ đỉnh kề đó
            if neighbor not in visited:
                if dfs(neighbor, target_vertex, visited):
                    return True
        
        # Nếu không tìm thấy đường đi từ đỉnh hiện tại đến đỉnh đích, trả về False
        return False
    
    # Khởi tạo tập hợp lưu trữ các đỉnh đã được thăm
    visited = set()
    
    # Bắt đầu DFS từ đỉnh v1 để kiểm tra có đường đi đến v2 hay không
    return dfs(v1, v2, visited)

# Ví dụ sử dụng
dt = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['A'],
    'D': ['A', 'C']
}

dinh1 = 'A'
dinh2 = 'D'
print("Có đường đi từ", dinh1, "đến", dinh2, "không?", DuongDi(dt, dinh1, dinh2))

### Bai 1
class Node:
    def __init__(self, data):
        self.Info = data
        self.Left = None
        self.Right = None

class CayNhiPhan:
    def __init__(self):
        self.root = None

    # Hàm đệ qui để đếm số nút của cây con
    def dem_so_nut(self, node):
        if node is None:
            return 0
        return 1 + self.dem_so_nut(node.Left) + self.dem_so_nut(node.Right)

    # Phương thức trả về số nút của cây
    def SoNut(self):
        return self.dem_so_nut(self.root)

# Ví dụ sử dụng:
# Tạo cây nhị phân
tree = CayNhiPhan()
tree.root = Node(1)
tree.root.Left = Node(2)
tree.root.Right = Node(3)
tree.root.Left.Left = Node(4)
tree.root.Left.Right = Node(5)

# In số nút của cây
print("Số nút của cây là:", tree.SoNut())  # Kết quả mong đợi: 5





### Bài 2
class Node:
    def __init__(self, data):
        self.Info = data
        self.Left = None
        self.Right = None

class CayNhiPhan:
    def __init__(self):
        self.root = None

    # Hàm đệ qui để tính chiều cao của cây
    def chieu_cao_cay(self, node):
        if node is None:
            return 0
        # Tính chiều cao của cây con bên trái và cây con bên phải
        chieu_cao_trai = self.chieu_cao_cay(node.Left)
        chieu_cao_phai = self.chieu_cao_cay(node.Right)
        # Trả về chiều cao lớn nhất cộng thêm 1 (đối với node hiện tại)
        return max(chieu_cao_trai, chieu_cao_phai) + 1

    # Phương thức trả về chiều cao của cây
    def ChieuCao(self):
        return self.chieu_cao_cay(self.root)

# Ví dụ sử dụng:
# Tạo cây nhị phân
tree = CayNhiPhan()
tree.root = Node(1)
tree.root.Left = Node(2)
tree.root.Right = Node(3)
tree.root.Left.Left = Node(4)
tree.root.Left.Right = Node(5)
tree.root.Right.Right = Node(6)

# In chiều cao của cây
print("Chiều cao của cây là:", tree.ChieuCao())  # Kết quả mong đợi: 3





### Bài 3
class Node:
    def __init__(self, data):
        self.Info = data
        self.Left = None
        self.Right = None

class CayNhiPhan:
    def __init__(self):
        self.root = None

    # Hàm đệ qui để đếm số nút lá của cây
    def dem_so_nut_la(self, node):
        if node is None:
            return 0
        # Nếu node là nút lá, trả về 1
        if node.Left is None and node.Right is None:
            return 1
        # Đệ qui đếm số nút lá của cây con bên trái và cây con bên phải
        return self.dem_so_nut_la(node.Left) + self.dem_so_nut_la(node.Right)

    # Phương thức trả về số nút lá của cây
    def SoNutLa(self):
        return self.dem_so_nut_la(self.root)

# Ví dụ sử dụng:
# Tạo cây nhị phân
tree = CayNhiPhan()
tree.root = Node(1)
tree.root.Left = Node(2)
tree.root.Right = Node(3)
tree.root.Left.Left = Node(4)
tree.root.Left.Right = Node(5)
tree.root.Right.Right = Node(6)
tree.root.Right.Right.Left = Node(7)

# In số nút lá của cây
print("Số nút lá của cây là:", tree.SoNutLa())  # Kết quả mong đợi: 3





#Bài 4
class Node:
    def __init__(self, data):
        self.Info = data
        self.Left = None
        self.Right = None

class CayNhiPhan:
    def __init__(self):
        self.root = None

    # Hàm đệ qui để đếm số nút trung gian của cây
    def dem_so_nut_trung_gian(self, node):
        if node is None:
            return 0
        # Nếu node không phải là nút lá và không phải là nút gốc, trả về 1
        if (node.Left is not None or node.Right is not None) and node is not self.root:
            return 1 + self.dem_so_nut_trung_gian(node.Left) + self.dem_so_nut_trung_gian(node.Right)
        # Đệ qui đếm số nút trung gian của cây con bên trái và cây con bên phải
        return self.dem_so_nut_trung_gian(node.Left) + self.dem_so_nut_trung_gian(node.Right)

    # Phương thức trả về số nút trung gian của cây
    def SoNutTrungGian(self):
        return self.dem_so_nut_trung_gian(self.root)

# Ví dụ sử dụng:
# Tạo cây nhị phân
tree = CayNhiPhan()
tree.root = Node(1)
tree.root.Left = Node(2)
tree.root.Right = Node(3)
tree.root.Left.Left = Node(4)
tree.root.Left.Right = Node(5)
tree.root.Right.Right = Node(6)
tree.root.Right.Right.Left = Node(7)

# In số nút trung gian của cây
print("Số nút trung gian của cây là:", tree.SoNutTrungGian())  # Kết quả mong đợi: 3





### Bài 5
class Node:
    def __init__(self, data):
        self.Info = data
        self.Left = None
        self.Right = None

class CayNhiPhan:
    def __init__(self):
        self.root = None

    # Hàm hỗ trợ kiểm tra BST
    def kiem_tra_bst_util(self, node, min_val, max_val):
        # Trường hợp cơ sở: nếu node là None, trả về True
        if node is None:
            return True
        
        # Kiểm tra giá trị của node phải nằm trong khoảng (min_val, max_val)
        if min_val < node.Info < max_val:
            # Kiểm tra BST cho cả hai cây con của node
            return (self.kiem_tra_bst_util(node.Left, min_val, node.Info) and
                    self.kiem_tra_bst_util(node.Right, node.Info, max_val))
        
        # Nếu node.Info không nằm trong khoảng (min_val, max_val), trả về False
        return False

    # Phương thức kiểm tra BST cho cây nhị phân
    def KiemTraBST(self):
        return self.kiem_tra_bst_util(self.root, float('-inf'), float('inf'))

# Ví dụ sử dụng:
# Tạo cây nhị phân BST
tree_bst = CayNhiPhan()
tree_bst.root = Node(4)
tree_bst.root.Left = Node(2)
tree_bst.root.Right = Node(5)
tree_bst.root.Left.Left = Node(1)
tree_bst.root.Left.Right = Node(3)

# Kiểm tra xem cây nhị phân có phải là BST không
print("Cây nhị phân là BST:", tree_bst.KiemTraBST())  # Kết quả mong đợi: True

# Tạo cây nhị phân không phải là BST
tree_not_bst = CayNhiPhan()
tree_not_bst.root = Node(3)
tree_not_bst.root.Left = Node(2)
tree_not_bst.root.Right = Node(5)
tree_not_bst.root.Left.Left = Node(1)
tree_not_bst.root.Left.Right = Node(4)

# Kiểm tra xem cây nhị phân có phải là BST không
print("Cây nhị phân là BST:", tree_not_bst.KiemTraBST())  # Kết quả mong đợi: False





### bài 6
class Node:
    def __init__(self, data):
        self.Info = data
        self.Left = None
        self.Right = None

class CayNhiPhan:
    def __init__(self):
        self.root = None

    # Hàm tính chiều cao của một cây nhị phân
    def chieu_cao(self, node):
        if node is None:
            return 0
        return max(self.chieu_cao(node.Left), self.chieu_cao(node.Right)) + 1

    # Hàm kiểm tra cây nhị phân có phải là cây AVL không
    def kiem_tra_avl(self, node):
        if node is None:
            return True
        
        # Tính chiều cao của cây con bên trái và cây con bên phải
        left_height = self.chieu_cao(node.Left)
        right_height = self.chieu_cao(node.Right)
        
        # Kiểm tra điều kiện cân bằng
        if abs(left_height - right_height) <= 1 and self.kiem_tra_avl(node.Left) and self.kiem_tra_avl(node.Right):
            return True
        
        return False

    # Phương thức kiểm tra AVL cho cây nhị phân
    def KiemTraAVL(self):
        return self.kiem_tra_avl(self.root)

# Ví dụ sử dụng:
# Tạo cây nhị phân AVL
tree_avl = CayNhiPhan()
tree_avl.root = Node(4)
tree_avl.root.Left = Node(2)
tree_avl.root.Right = Node(6)
tree_avl.root.Left.Left = Node(1)
tree_avl.root.Left.Right = Node(3)
tree_avl.root.Right.Left = Node(5)
tree_avl.root.Right.Right = Node(7)

# Kiểm tra xem cây nhị phân có phải là AVL không
print("Cây nhị phân là AVL:", tree_avl.KiemTraAVL())  # Kết quả mong đợi: True

# Tạo cây nhị phân không phải là AVL
tree_not_avl = CayNhiPhan()
tree_not_avl.root = Node(4)
tree_not_avl.root.Left = Node(2)
tree_not_avl.root.Right = Node(6)
tree_not_avl.root.Left.Left = Node(1)
tree_not_avl.root.Left.Right = Node(3)
tree_not_avl.root.Left.Left.Left = Node(0)

# Kiểm tra xem cây nhị phân có phải là AVL không
print("Cây nhị phân là AVL:", tree_not_avl.KiemTraAVL())  # Kết quả mong đợi: False





### Bài 7
class Node:
    def __init__(self, data):
        self.Info = data
        self.Left = None
        self.Right = None

class CayNhiPhan:
    def __init__(self):
        self.root = None

    # Phương thức hỗ trợ để sao chép một cây nhị phân
    def sao_chep_util(self, old_node):
        if old_node is None:
            return None
        
        # Tạo một nút mới với thông tin từ nút cũ
        new_node = Node(old_node.Info)
        # Đệ quy sao chép các cây con bên trái và bên phải của nút cũ
        new_node.Left = self.sao_chep_util(old_node.Left)
        new_node.Right = self.sao_chep_util(old_node.Right)
        
        return new_node

    # Phương thức sao chép cây nhị phân
    def Chep(self):
        # Gọi hàm hỗ trợ để sao chép cây
        return self.sao_chep_util(self.root)

# Ví dụ sử dụng:
# Tạo cây nhị phân gốc
tree = CayNhiPhan()
tree.root = Node(1)
tree.root.Left = Node(2)
tree.root.Right = Node(3)
tree.root.Left.Left = Node(4)
tree.root.Left.Right = Node(5)

# Sao chép cây nhị phân
copied_tree = tree.Chep()

# In cây nhị phân gốc
print("Cây nhị phân gốc:")
# Code in cây nhị phân đã được cung cấp ở trên (tùy thuộc vào cách bạn muốn hiển thị cây)

# In cây nhị phân sao chép
print("\nCây nhị phân sao chép:")
# Code in cây nhị phân đã được cung cấp ở trên (tùy thuộc vào cách bạn muốn hiển thị cây)





### Bài 8
class Node:
    def __init__(self, data):
        self.Info = data
        self.Left = None
        self.Right = None

class CayNhiPhan:
    def __init__(self):
        self.root = None

    # Phương thức hỗ trợ để so sánh hai cây nhị phân
    def so_sanh_util(self, node1, node2):
        # Nếu cả hai nút đều là None thì chúng giống nhau
        if node1 is None and node2 is None:
            return True
        # Nếu chỉ một trong hai nút là None thì chúng khác nhau
        if node1 is None or node2 is None:
            return False
        
        # So sánh giá trị của hai nút và các cây con của chúng
        return (node1.Info == node2.Info and
                self.so_sanh_util(node1.Left, node2.Left) and
                self.so_sanh_util(node1.Right, node2.Right))

    # Phương thức so sánh hai cây nhị phân
    def SoSanh(self, other_tree):
        # Gọi hàm hỗ trợ để so sánh hai cây
        return self.so_sanh_util(self.root, other_tree.root)

# Ví dụ sử dụng:
# Tạo cây nhị phân thứ nhất
tree1 = CayNhiPhan()
tree1.root = Node(1)
tree1.root.Left = Node(2)
tree1.root.Right = Node(3)

# Tạo cây nhị phân thứ hai, giống hệt cây nhị phân thứ nhất
tree2 = CayNhiPhan()
tree2.root = Node(1)
tree2.root.Left = Node(2)
tree2.root.Right = Node(3)

# Tạo cây nhị phân thứ ba, khác biệt so với cây nhị phân thứ nhất
tree3 = CayNhiPhan()
tree3.root = Node(1)
tree3.root.Left = Node(3)
tree3.root.Right = Node(2)

# So sánh cây nhị phân thứ nhất với cây nhị phân thứ hai
print("Cây 1 và cây 2 giống hệt nhau:", tree1.SoSanh(tree2))  # Kết quả mong đợi: True

# So sánh cây nhị phân thứ nhất với cây nhị phân thứ ba
print("Cây 1 và cây 3 giống hệt nhau:", tree1.SoSanh(tree3))  # Kết quả mong đợi: False





### Bài 9
class Node:
    def __init__(self, data):
        self.Info = data
        self.Left = None
        self.Right = None

class CayNhiPhan:
    def __init__(self):
        self.root = None

    # Phương thức hỗ trợ để kiểm tra xem một cây có phải là cây con của cây khác không
    def la_cay_con_util(self, node1, node2):
        # Nếu node2 là None thì node2 là cây con của node1
        if node2 is None:
            return True
        # Nếu node1 là None nhưng node2 không phải là None thì node2 không phải là cây con của node1
        if node1 is None:
            return False

        # Nếu giá trị của hai nút khác nhau thì node2 không phải là cây con của node1
        if node1.Info != node2.Info:
            return False

        # Kiểm tra tiếp các cây con bên trái và bên phải của node1 và node2
        return (self.la_cay_con_util(node1.Left, node2.Left) and
                self.la_cay_con_util(node1.Right, node2.Right))

    # Phương thức kiểm tra xem một cây có phải là cây con của cây khác không
    def CayCon(self, other_tree):
        # Gọi hàm hỗ trợ để kiểm tra xem other_tree có phải là cây con của self không
        return self.la_cay_con_util(self.root, other_tree.root)

# Ví dụ sử dụng:
# Tạo cây nhị phân thứ nhất
tree1 = CayNhiPhan()
tree1.root = Node(1)
tree1.root.Left = Node(2)
tree1.root.Right = Node(3)

# Tạo cây nhị phân thứ hai, là cây con của cây nhị phân thứ nhất
tree2 = CayNhiPhan()
tree2.root = Node(2)

# Tạo cây nhị phân thứ ba, không phải là cây con của cây nhị phân thứ nhất
tree3 = CayNhiPhan()
tree3.root = Node(4)
tree3.root.Left = Node(2)
tree3.root.Right = Node(5)

# Kiểm tra xem cây nhị phân thứ hai có phải là cây con của cây nhị phân thứ nhất không
print("Cây 2 là cây con của cây 1:", tree1.CayCon(tree2))  # Kết quả mong đợi: True

# Kiểm tra xem cây nhị phân thứ ba có phải là cây con của cây nhị phân thứ nhất không
print("Cây 3 là cây con của cây 1:", tree1.CayCon(tree3))  # Kết quả mong đợi: False





### bài 10
class Node:
    def __init__(self, data):
        self.Info = data
        self.Left = None
        self.Right = None

class CayNhiPhan:
    def __init__(self):
        self.root = None

    # Phương thức tính chiều cao của một cây
    def ChieuCao(self, node):
        if node is None:
            return 0
        return max(self.ChieuCao(node.Left), self.ChieuCao(node.Right)) + 1

    # Phương thức kiểm tra xem một cây có cân bằng hoàn toàn không
    def CanBangHoanToan(self):
        return self.kiem_tra_can_bang_hoan_toan_util(self.root)

    # Hàm hỗ trợ để kiểm tra cân bằng hoàn toàn
    def kiem_tra_can_bang_hoan_toan_util(self, node):
        if node is None:
            return True

        # Kiểm tra chiều cao của cây con bên trái và cây con bên phải
        chieu_cao_left = self.ChieuCao(node.Left)
        chieu_cao_right = self.ChieuCao(node.Right)

        # Nếu chênh lệch chiều cao lớn hơn 1, cây không cân bằng hoàn toàn
        if abs(chieu_cao_left - chieu_cao_right) > 1:
            return False

        # Kiểm tra cân bằng hoàn toàn ở cây con bên trái và cây con bên phải
        return (self.kiem_tra_can_bang_hoan_toan_util(node.Left) and
                self.kiem_tra_can_bang_hoan_toan_util(node.Right))

# Ví dụ sử dụng:
# Tạo cây nhị phân cân bằng hoàn toàn
tree = CayNhiPhan()
tree.root = Node(1)
tree.root.Left = Node(2)
tree.root.Right = Node(3)
tree.root.Left.Left = Node(4)
tree.root.Left.Right = Node(5)
tree.root.Right.Left = Node(6)
tree.root.Right.Right = Node(7)

# Kiểm tra xem cây có cân bằng hoàn toàn không
print("Cây có cân bằng hoàn toàn:", tree.CanBangHoanToan())  # Kết quả mong đợi: True





### bài 11
class Node:
    def __init__(self, data):
        self.Info = data
        self.Left = None
        self.Right = None

class CayNhiPhan:
    def __init__(self):
        self.root = None

    # Phương thức kiểm tra xem một cây có phải là cây BST tuần tự không
    def BSTTuanTu(self):
        return self.kiem_tra_bst_tuan_tu_util(self.root)

    # Hàm hỗ trợ để kiểm tra cây BST tuần tự
    def kiem_tra_bst_tuan_tu_util(self, node):
        if node is None:
            return True
        
        # Kiểm tra xem nút có nút con bên trái không hoặc có nút con bên phải không
        if (node.Left is not None and node.Right is not None) or (node.Left is None and node.Right is None):
            return self.kiem_tra_bst_tuan_tu_util(node.Left) and self.kiem_tra_bst_tuan_tu_util(node.Right)
        
        return False

# Ví dụ sử dụng:
# Tạo một cây BST tuần tự
tree = CayNhiPhan()
tree.root = Node(4)
tree.root.Left = Node(2)
tree.root.Right = Node(6)
tree.root.Left.Left = Node(1)
tree.root.Left.Right = Node(3)
tree.root.Right.Right = Node(7)

# Kiểm tra xem cây có phải là cây BST tuần tự không
print("Cây là cây BST tuần tự:", tree.BSTTuanTu())  # Kết quả mong đợi: True


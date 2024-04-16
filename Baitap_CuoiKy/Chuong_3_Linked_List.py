### Câu 1
class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
        self.KeTiep = None

class DaThuc:
    def __init__(self):
        self.Head = None

    def Them(self, heso, somu):
        new_node = Node(heso, somu)

        # Nếu danh sách đang trống, gán nút mới làm đầu
        if self.Head is None:
            self.Head = new_node
            return

        # Nếu số mũ của số hạng mới lớn hơn số mũ của số hạng đầu tiên
        # Thêm số hạng mới vào đầu danh sách
        if somu > self.Head.SoMu:
            new_node.KeTiep = self.Head
            self.Head = new_node
            return

        current = self.Head
        # Tìm vị trí phù hợp để chèn số hạng mới
        while current.KeTiep is not None and current.KeTiep.SoMu > somu:
            current = current.KeTiep
        
        # Chèn số hạng mới vào vị trí tìm được
        new_node.KeTiep = current.KeTiep
        current.KeTiep = new_node

    def XuatDaThuc(self):
        current = self.Head
        while current:
            print(f"{current.HeSo}*x^{current.SoMu}", end=" ")
            if current.KeTiep:
                print("+", end=" ")
            current = current.KeTiep
        print()

# Ví dụ sử dụng:
dathuc = DaThuc()

# Thêm các số hạng vào đa thức
dathuc.Them(3, 2)
dathuc.Them(5, 1)
dathuc.Them(2, 4)
dathuc.Them(1, 3)

# In ra đa thức
dathuc.XuatDaThuc()





### Câu 2
class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
        self.KeTiep = None

class DaThuc:
    def __init__(self):
        self.Head = None

    def Them(self, heso, somu):
        new_node = Node(heso, somu)

        # Nếu danh sách đang trống, gán nút mới làm đầu
        if self.Head is None:
            self.Head = new_node
            return

        # Nếu số mũ của số hạng mới lớn hơn số mũ của số hạng đầu tiên
        # Thêm số hạng mới vào đầu danh sách
        if somu > self.Head.SoMu:
            new_node.KeTiep = self.Head
            self.Head = new_node
            return

        current = self.Head
        # Tìm vị trí phù hợp để chèn số hạng mới
        while current.KeTiep is not None and current.KeTiep.SoMu > somu:
            current = current.KeTiep
        
        # Chèn số hạng mới vào vị trí tìm được
        new_node.KeTiep = current.KeTiep
        current.KeTiep = new_node

    def RutGon(self):
        # Duyệt qua các số hạng trong đa thức
        current = self.Head
        while current and current.KeTiep:
            # Nếu có hai số hạng có cùng số mũ
            if current.SoMu == current.KeTiep.SoMu:
                # Cộng hai số hạng có cùng số mũ
                current.HeSo += current.KeTiep.HeSo
                # Loại bỏ số hạng thứ hai
                current.KeTiep = current.KeTiep.KeTiep
            else:
                # Chuyển sang số hạng tiếp theo
                current = current.KeTiep
        
        # Loại bỏ các số hạng có hệ số bằng 0
        current = self.Head
        previous = None
        while current:
            if current.HeSo == 0:
                if previous:
                    previous.KeTiep = current.KeTiep
                else:
                    self.Head = current.KeTiep
            else:
                previous = current
            current = current.KeTiep

    def XuatDaThuc(self):
        current = self.Head
        while current:
            print(f"{current.HeSo}*x^{current.SoMu}", end=" ")
            if current.KeTiep:
                print("+", end=" ")
            current = current.KeTiep
        print()

# Ví dụ sử dụng:
dathuc = DaThuc()

# Thêm các số hạng vào đa thức
dathuc.Them(3, 2)
dathuc.Them(-2, 3)
dathuc.Them(5, 1)
dathuc.Them(-2, 3)
dathuc.Them(2, 4)
dathuc.Them(0, 3)

# In ra đa thức trước khi rút gọn
print("Đa thức trước khi rút gọn:")
dathuc.XuatDaThuc()

# Rút gọn đa thức
dathuc.RutGon()

# In ra đa thức sau khi rút gọn
print("\nĐa thức sau khi rút gọn:")
dathuc.XuatDaThuc()





### Câu 3
class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
        self.KeTiep = None

class DaThuc:
    def __init__(self):
        self.Head = None

    def Them(self, heso, somu):
        new_node = Node(heso, somu)

        # Nếu danh sách đang trống, gán nút mới làm đầu
        if self.Head is None:
            self.Head = new_node
            return

        # Nếu số mũ của số hạng mới lớn hơn số mũ của số hạng đầu tiên
        # Thêm số hạng mới vào đầu danh sách
        if somu > self.Head.SoMu:
            new_node.KeTiep = self.Head
            self.Head = new_node
            return

        current = self.Head
        # Tìm vị trí phù hợp để chèn số hạng mới
        while current.KeTiep is not None and current.KeTiep.SoMu > somu:
            current = current.KeTiep
        
        # Chèn số hạng mới vào vị trí tìm được
        new_node.KeTiep = current.KeTiep
        current.KeTiep = new_node

    def RutGon(self):
        # Duyệt qua các số hạng trong đa thức
        current = self.Head
        while current and current.KeTiep:
            # Nếu có hai số hạng có cùng số mũ
            if current.SoMu == current.KeTiep.SoMu:
                # Cộng hai số hạng có cùng số mũ
                current.HeSo += current.KeTiep.HeSo
                # Loại bỏ số hạng thứ hai
                current.KeTiep = current.KeTiep.KeTiep
            else:
                # Chuyển sang số hạng tiếp theo
                current = current.KeTiep
        
        # Loại bỏ các số hạng có hệ số bằng 0
        current = self.Head
        previous = None
        while current:
            if current.HeSo == 0:
                if previous:
                    previous.KeTiep = current.KeTiep
                else:
                    self.Head = current.KeTiep
            else:
                previous = current
            current = current.KeTiep

    def Cong(self, dathuc):
        result = DaThuc()

        # Duyệt qua cả hai đa thức
        current1 = self.Head
        current2 = dathuc.Head
        while current1 and current2:
            # Nếu số mũ của số hạng đa thức thứ nhất lớn hơn số mũ của số hạng thứ hai
            # Thêm số hạng của đa thức thứ nhất vào kết quả và di chuyển đến số hạng tiếp theo của đa thức thứ nhất
            if current1.SoMu > current2.SoMu:
                result.Them(current1.HeSo, current1.SoMu)
                current1 = current1.KeTiep
            # Nếu số mũ của số hạng đa thức thứ hai lớn hơn số mũ của số hạng thứ nhất
            # Thêm số hạng của đa thức thứ hai vào kết quả và di chuyển đến số hạng tiếp theo của đa thức thứ hai
            elif current1.SoMu < current2.SoMu:
                result.Them(current2.HeSo, current2.SoMu)
                current2 = current2.KeTiep
            # Nếu số mũ của cả hai số hạng bằng nhau
            else:
                # Thêm số hạng có tổng hệ số vào kết quả và di chuyển đến số hạng tiếp theo của cả hai đa thức
                result.Them(current1.HeSo + current2.HeSo, current1.SoMu)
                current1 = current1.KeTiep
                current2 = current2.KeTiep
        
        # Duyệt qua số hạng còn lại của đa thức thứ nhất (nếu có)
        while current1:
            result.Them(current1.HeSo, current1.SoMu)
            current1 = current1.KeTiep
        
        # Duyệt qua số hạng còn lại của đa thức thứ hai (nếu có)
        while current2:
            result.Them(current2.HeSo, current2.SoMu)
            current2 = current2.KeTiep
        
        # Rút gọn đa thức kết quả
        result.RutGon()

        return result

    def XuatDaThuc(self):
        current = self.Head
        while current:
            print(f"{current.HeSo}*x^{current.SoMu}", end=" ")
            if current.KeTiep:
                print("+", end=" ")
            current = current.KeTiep
        print()

# Ví dụ sử dụng:
dathuc1 = DaThuc()
dathuc2 = DaThuc()

# Thêm các số hạng vào đa thức thứ nhất
dathuc1.Them(3, 2)
dathuc1.Them(5, 1)
dathuc1.Them(2, 4)
dathuc1.Them(1, 3)

# Thêm các số hạng vào đa thức thứ hai
dathuc2.Them(2, 2)
dathuc2.Them(4, 1)
dathuc2.Them(1, 4)

# In ra đa thức thứ nhất và thứ hai trước khi cộng
print("Đa thức thứ nhất:")
dathuc1.XuatDaThuc()
print("\nĐa thức thứ hai:")
dathuc2.XuatDaThuc()

# Cộng hai đa thức và in ra kết quả
dathuc_tong = dathuc1.Cong(dathuc2)
print("\nĐa thức sau khi cộng:")
dathuc_tong.XuatDaThuc()





### Câu 4
class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
        self.KeTiep = None

class DaThuc:
    def __init__(self):
        self.Head = None

    def Them(self, heso, somu):
        new_node = Node(heso, somu)

        # Nếu danh sách đang trống, gán nút mới làm đầu
        if self.Head is None:
            self.Head = new_node
            return

        # Nếu số mũ của số hạng mới lớn hơn số mũ của số hạng đầu tiên
        # Thêm số hạng mới vào đầu danh sách
        if somu > self.Head.SoMu:
            new_node.KeTiep = self.Head
            self.Head = new_node
            return

        current = self.Head
        # Tìm vị trí phù hợp để chèn số hạng mới
        while current.KeTiep is not None and current.KeTiep.SoMu > somu:
            current = current.KeTiep
        
        # Chèn số hạng mới vào vị trí tìm được
        new_node.KeTiep = current.KeTiep
        current.KeTiep = new_node

    def DoiDau(self):
        # Duyệt qua các số hạng trong đa thức và đổi ngược dấu của hệ số
        current = self.Head
        while current:
            current.HeSo = -current.HeSo
            current = current.KeTiep

    def XuatDaThuc(self):
        current = self.Head
        while current:
            print(f"{current.HeSo}*x^{current.SoMu}", end=" ")
            if current.KeTiep:
                print("+", end=" ")
            current = current.KeTiep
        print()

# Ví dụ sử dụng:
dathuc = DaThuc()

# Thêm các số hạng vào đa thức
dathuc.Them(3, 2)
dathuc.Them(-5, 1)
dathuc.Them(2, 4)
dathuc.Them(-1, 3)

# In ra đa thức trước khi đổi dấu
print("Đa thức trước khi đổi dấu:")
dathuc.XuatDaThuc()

# Đổi dấu các số hạng trong đa thức và in ra kết quả
dathuc.DoiDau()
print("\nĐa thức sau khi đổi dấu:")
dathuc.XuatDaThuc()





### Câu 5
class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
        self.KeTiep = None

class DaThuc:
    def __init__(self):
        self.Head = None

    def Them(self, heso, somu):
        new_node = Node(heso, somu)

        # Nếu danh sách đang trống, gán nút mới làm đầu
        if self.Head is None:
            self.Head = new_node
            return

        # Nếu số mũ của số hạng mới lớn hơn số mũ của số hạng đầu tiên
        # Thêm số hạng mới vào đầu danh sách
        if somu > self.Head.SoMu:
            new_node.KeTiep = self.Head
            self.Head = new_node
            return

        current = self.Head
        # Tìm vị trí phù hợp để chèn số hạng mới
        while current.KeTiep is not None and current.KeTiep.SoMu > somu:
            current = current.KeTiep
        
        # Chèn số hạng mới vào vị trí tìm được
        new_node.KeTiep = current.KeTiep
        current.KeTiep = new_node

    def RutGon(self):
        # Duyệt qua các số hạng trong đa thức
        current = self.Head
        while current and current.KeTiep:
            # Nếu có hai số hạng có cùng số mũ
            if current.SoMu == current.KeTiep.SoMu:
                # Cộng hai số hạng có cùng số mũ
                current.HeSo += current.KeTiep.HeSo
                # Loại bỏ số hạng thứ hai
                current.KeTiep = current.KeTiep.KeTiep
            else:
                # Chuyển sang số hạng tiếp theo
                current = current.KeTiep
        
        # Loại bỏ các số hạng có hệ số bằng 0
        current = self.Head
        previous = None
        while current:
            if current.HeSo == 0:
                if previous:
                    previous.KeTiep = current.KeTiep
                else:
                    self.Head = current.KeTiep
            else:
                previous = current
            current = current.KeTiep

    def Tich(self, dathuc):
        result = DaThuc()

        # Duyệt qua từng số hạng của đa thức thứ nhất
        current1 = self.Head
        while current1:
            # Duyệt qua từng số hạng của đa thức thứ hai
            current2 = dathuc.Head
            while current2:
                # Nhân hệ số của số hạng thứ nhất với hệ số của số hạng thứ hai
                heso_moi = current1.HeSo * current2.HeSo
                # Cộng số mũ của số hạng thứ nhất và số mũ của số hạng thứ hai
                somu_moi = current1.SoMu + current2.SoMu
                # Thêm số hạng mới vào kết quả
                result.Them(heso_moi, somu_moi)
                # Di chuyển đến số hạng tiếp theo của đa thức thứ hai
                current2 = current2.KeTiep
            
            # Di chuyển đến số hạng tiếp theo của đa thức thứ nhất
            current1 = current1.KeTiep
        
        # Rút gọn đa thức kết quả
        result.RutGon()

        return result

    def XuatDaThuc(self):
        current = self.Head
        while current:
            print(f"{current.HeSo}*x^{current.SoMu}", end=" ")
            if current.KeTiep:
                print("+", end=" ")
            current = current.KeTiep
        print()

# Ví dụ sử dụng:
dathuc1 = DaThuc()
dathuc2 = DaThuc()

# Thêm các số hạng vào đa thức thứ nhất
dathuc1.Them(3, 2)
dathuc1.Them(5, 1)

# Thêm các số hạng vào đa thức thứ hai
dathuc2.Them(2, 2)
dathuc2.Them(4, 1)

# In ra đa thức thứ nhất và thứ hai trước khi tính tích
print("Đa thức thứ nhất:")
dathuc1.XuatDaThuc()
print("\nĐa thức thứ hai:")
dathuc2.XuatDaThuc()

# Tính tích của hai đa thức và in ra kết quả
dathuc_tich = dathuc1.Tich(dathuc2)
print("\nĐa thức sau khi tính tích:")
dathuc_tich.XuatDaThuc()





### Câu 6
class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
        self.KeTiep = None

class DaThuc:
    def __init__(self):
        self.Head = None

    def Them(self, heso, somu):
        new_node = Node(heso, somu)

        # Nếu danh sách đang trống, gán nút mới làm đầu
        if self.Head is None:
            self.Head = new_node
            return

        # Nếu số mũ của số hạng mới lớn hơn số mũ của số hạng đầu tiên
        # Thêm số hạng mới vào đầu danh sách
        if somu > self.Head.SoMu:
            new_node.KeTiep = self.Head
            self.Head = new_node
            return

        current = self.Head
        # Tìm vị trí phù hợp để chèn số hạng mới
        while current.KeTiep is not None and current.KeTiep.SoMu > somu:
            current = current.KeTiep
        
        # Chèn số hạng mới vào vị trí tìm được
        new_node.KeTiep = current.KeTiep
        current.KeTiep = new_node

    def Chep(self):
        # Tạo một đa thức mới để sao chép dữ liệu
        result = DaThuc()
        current = self.Head

        # Duyệt qua từng số hạng trong đa thức gốc và thêm vào đa thức sao chép
        while current:
            result.Them(current.HeSo, current.SoMu)
            current = current.KeTiep

        return result

    def XuatDaThuc(self):
        current = self.Head
        while current:
            print(f"{current.HeSo}*x^{current.SoMu}", end=" ")
            if current.KeTiep:
                print("+", end=" ")
            current = current.KeTiep
        print()

# Ví dụ sử dụng:
dathuc = DaThuc()

# Thêm các số hạng vào đa thức
dathuc.Them(3, 2)
dathuc.Them(-5, 1)
dathuc.Them(2, 4)
dathuc.Them(1, 3)

# Sao chép đa thức và in ra kết quả
dathuc_copy = dathuc.Chep()
print("Đa thức sau khi sao chép:")
dathuc_copy.XuatDaThuc()


### Câu 1

class Node:
    def __init__(self, data):
        self.Info = data
        self.Next = None

class DSLK:
    def __init__(self):
        self.Head = None

    def Them(self, data):
        new_node = Node(data)
        new_node.Next = self.Head
        self.Head = new_node

    def InNguoc_DeQui(self, node):
        if node is None:
            return
        self.InNguoc_DeQui(node.Next)
        print(node.Info, end=" ")

    def InNguoc_KhongDeQui(self):
        stack = []
        current = self.Head
        # Đưa tất cả các phần tử vào stack
        while current:
            stack.append(current)
            current = current.Next
        # In ra các phần tử từ stack
        while stack:
            node = stack.pop()
            print(node.Info, end=" ")

# Ví dụ sử dụng:
dslk = DSLK()
dslk.Them(1)
dslk.Them(2)
dslk.Them(5)
dslk.Them(4)

print("In ngược danh sách liên kết (sử dụng đệ qui):")
dslk.InNguoc_DeQui(dslk.Head)
print("\nIn ngược danh sách liên kết (sử dụng stack):")
dslk.InNguoc_KhongDeQui()





### Câu 2
class Node:
    def __init__(self, data):
        self.Info = data
        self.Next = None

class DSLK:
    def __init__(self):
        self.Head = None

    def Them(self, data):
        new_node = Node(data)
        new_node.Next = self.Head
        self.Head = new_node

    def DaoNguoc(self):
        # Khởi tạo stack để lưu trữ các nút của danh sách liên kết
        stack = []
        current = self.Head
        # Đưa tất cả các nút vào stack
        while current:
            stack.append(current)
            current = current.Next
        # Lấy nút đầu tiên của danh sách mới
        self.Head = stack.pop()
        current = self.Head
        # Lấy các nút từ stack để đảo ngược danh sách liên kết
        while stack:
            current.Next = stack.pop()
            current = current.Next
        # Đặt con trỏ của nút cuối cùng thành None để kết thúc danh sách liên kết
        current.Next = None

    def XuatDSLK(self):
        current = self.Head
        while current:
            print(current.Info, end=" ")
            current = current.Next
        print()

# Ví dụ sử dụng:
dslk = DSLK()
dslk.Them(1)
dslk.Them(2)
dslk.Them(3)
dslk.Them(4)

print("Danh sách liên kết trước khi đảo ngược:")
dslk.XuatDSLK()

dslk.DaoNguoc()

print("Danh sách liên kết sau khi đảo ngược:")
dslk.XuatDSLK()





### Câu 3
class BT:
    def __init__(self, expression):
        self.expression = expression

    def GiaTri(self):
        # Hàm tính giá trị của biểu thức con
        def tinh(pheptoan, op1, op2):
            if pheptoan == '+':
                return op1 + op2
            elif pheptoan == '-':
                return op1 - op2
            elif pheptoan == '*':
                return op1 * op2
            elif pheptoan == '/':
                return op1 / op2

        # Chuyển biểu thức thành danh sách các thành phần (toán tử và toán hạng)
        components = self.expression.split()

        # Chồng để lưu trữ các toán hạng
        operand_stack = []
        # Chồng để lưu trữ các toán tử
        operator_stack = []

        # Duyệt qua từng thành phần trong biểu thức
        for component in components:
            # Nếu thành phần là toán tử, đẩy vào chồng toán tử
            if component in ['+', '-', '*', '/']:
                operator_stack.append(component)
            else:  # Nếu thành phần là toán hạng
                operand_stack.append(float(component))
                # Nếu chồng toán hạng và toán tử không rỗng và có đủ hai toán hạng
                while len(operand_stack) >= 2 and len(operator_stack) >= 1:
                    # Lấy hai toán hạng và một toán tử từ chồng
                    op2 = operand_stack.pop()
                    op1 = operand_stack.pop()
                    operator = operator_stack.pop()
                    # Thực hiện phép toán và đẩy kết quả vào chồng toán hạng
                    operand_stack.append(tinh(operator, op1, op2))

        # Kết quả cuối cùng là toán hạng còn lại trong chồng toán hạng
        return operand_stack[-1]

# Ví dụ sử dụng:
bt = BT("3 + 4 * 2 - 6 / 2")
print("Giá trị của biểu thức là:", bt.GiaTri())  # Kết quả mong đợi: 9.0





### Câu 4
class BT:
    def __init__(self, expression):
        self.expression = expression

    def HauTo(self):
        # Hàm xác định độ ưu tiên của phép toán
        def uuTien(pheptoan):
            if pheptoan in ['+', '-']:
                return 1
            elif pheptoan in ['*', '/']:
                return 2
            return 0

        # Chuyển biểu thức thành danh sách các thành phần (toán tử và toán hạng)
        components = self.expression.split()

        # Chồng để lưu trữ kết quả cuối cùng
        output_stack = []
        # Chồng để lưu trữ các toán tử
        operator_stack = []

        # Duyệt qua từng thành phần trong biểu thức
        for component in components:
            # Nếu thành phần là toán hạng, thêm vào danh sách kết quả
            if component not in ['+', '-', '*', '/']:
                output_stack.append(component)
            else:  # Nếu thành phần là toán tử
                # Kiểm tra độ ưu tiên của toán tử hiện tại so với toán tử đầu tiên trong chồng
                while operator_stack and uuTien(operator_stack[-1]) >= uuTien(component):
                    # Nếu độ ưu tiên của toán tử đầu tiên trong chồng lớn hơn hoặc bằng toán tử hiện tại
                    # Thì lấy toán tử đó ra khỏi chồng và thêm vào danh sách kết quả
                    output_stack.append(operator_stack.pop())
                # Thêm toán tử hiện tại vào chồng toán tử
                operator_stack.append(component)

        # Thêm các toán tử còn lại vào danh sách kết quả
        while operator_stack:
            output_stack.append(operator_stack.pop())

        # Kết quả cuối cùng là chuỗi biểu thức hậu tố
        return ' '.join(output_stack)

# Ví dụ sử dụng:
bt = BT("2 + 3 * 5")
print("Biểu thức hậu tố tương ứng là:", bt.HauTo())  # Kết quả mong đợi: '2 3 5 * +'





### câu 5
class HanoiTower:
    def __init__(self, n):
        self.n = n
        self.tower = [[], [], []]
        # Khởi tạo tháp ban đầu ở vị trí 1
        for i in range(n, 0, -1):
            self.tower[0].append(i)

    def move_disk(self, source, destination):
        # Di chuyển tầng trên cùng từ nguồn đến đích
        disk = self.tower[source].pop()
        self.tower[destination].append(disk)
        print(f"Di chuyển tầng {disk} từ tháp {source + 1} đến tháp {destination + 1}")

    def hanoi(self, n, source, destination, auxiliary):
        if n == 1:
            self.move_disk(source, destination)
            return
        self.hanoi(n - 1, source, auxiliary, destination)
        self.move_disk(source, destination)
        self.hanoi(n - 1, auxiliary, destination, source)

    def move_tower(self):
        print("Di chuyển tháp từ vị trí 1 đến vị trí 3 thông qua vị trí trung gian 2:")
        self.hanoi(self.n, 0, 2, 1)

# Ví dụ sử dụng:
n = 3  # Số tầng của tháp
hanoi_tower = HanoiTower(n)
hanoi_tower.move_tower()



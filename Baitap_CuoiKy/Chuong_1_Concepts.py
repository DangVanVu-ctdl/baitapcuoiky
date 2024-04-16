### Câu 1:

#Theo giải thuật đệ quy
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Nhập vào số nguyên n
n = int(input("Nhập vào số nguyên n >= 0: "))

# In ra số Fibonacci bậc 1 tương ứng với n sử dụng đệ qui
print("Số Fibonacci bậc 1 của", n, "là:", fibonacci_recursive(n))

#không đệ quy
def fibonacci_non_recursive(n):
    if n <= 1:
        return n
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i-1] + fib[i-2])
        return fib[n]

# Nhập vào số nguyên n
n = int(input("Nhập vào số nguyên n >= 0: "))

# In ra số Fibonacci bậc 1 tương ứng với n sử dụng không đệ qui
print("Số Fibonacci bậc 1 của", n, "là:", fibonacci_non_recursive(n))





### Câu 2:
def Neper(n):
    # Khởi tạo tổng ban đầu
    total = 0
    
    # Tính tổng từ a0 đến an
    for k in range(n + 1):
        total += 1 / factorial(k)
    
    return total

def factorial(k):
    # Tính giai thừa của k
    if k == 0:
        return 1
    else:
        result = 1
        for i in range(1, k + 1):
            result *= i
        return result

# Nhập vào số nguyên n
n = int(input("Nhập vào số nguyên n >= 0: "))

# In ra tổng của a0 + a1 + ... + an
print("Tổng của a0 + a1 + ... + an là:", Neper(n))





###Câu3
def GCD_recursive(m, n):
    if n == 0:
        return m
    else:
        return GCD_recursive(n, m % n)

# Nhập vào hai số nguyên dương m và n
m = int(input("Nhập vào số nguyên dương m: "))
n = int(input("Nhập vào số nguyên dương n: "))

# In ra ước số chung lớn nhất của m và n sử dụng đệ qui
print("Ước số chung lớn nhất của", m, "và", n, "là:", GCD_recursive(m, n))

#không đệ quy
def GCD_non_recursive(m, n):
    while n != 0:
        m, n = n, m % n
    return m

# Nhập vào hai số nguyên dương m và n
m = int(input("Nhập vào số nguyên dương m: "))
n = int(input("Nhập vào số nguyên dương n: "))

# In ra ước số chung lớn nhất của m và n sử dụng không đệ qui
print("Ước số chung lớn nhất của", m, "và", n, "là:", GCD_non_recursive(m, n))





### Câu 4:
def Pascal(n):
    # Khởi tạo một ma trận chứa các giá trị của tam giác Pascal
    triangle = []
    
    # Tạo ma trận tam giác Pascal
    for i in range(n):
        row = [1]  # Giá trị đầu tiên của mỗi hàng luôn là 1
        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)  # Giá trị cuối cùng của mỗi hàng luôn là 1
        triangle.append(row)
    
    # In ra tam giác Pascal
    for i, row in enumerate(triangle):
        print("n=", i, " ".join(str(x) for x in row))

# Nhập vào số nguyên dương n
n = int(input("Nhập vào số nguyên dương n: "))

# In ra tam giác Pascal ứng với bậc n
Pascal(n)





### Câu 5:
def Number(x, y):
    for n in range(x, y + 1):
        sum_divisors = sum_divisors_of(n)
        if sum_divisors < n:
            print(f"{n} là deficient")
        elif sum_divisors == n:
            print(f"{n} là perfect")
        else:
            print(f"{n} là abundant")

def sum_divisors_of(n):
    # Tính tổng các ước số của n
    total = 1  # 1 luôn là ước số của mọi số nguyên dương
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:  # Tránh trường hợp i và n // i là cùng một ước số (ví dụ: n = 4)
                total += n // i
    return total

# Nhập vào hai số nguyên dương x và y
x = int(input("Nhập vào số nguyên dương x: "))
y = int(input("Nhập vào số nguyên dương y (x ≤ y): "))

# Kiểm tra và in ra phân loại của các số từ x đến y
Number(x, y)

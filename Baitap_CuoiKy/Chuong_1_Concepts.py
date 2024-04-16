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
### bài 1
def Duynhat(a):
    # Sử dụng một tập hợp để loại bỏ các phần tử trùng nhau và giữ thứ tự tăng dần
    unique_set = set(a)
    # Sắp xếp các phần tử trong tập hợp để có thứ tự tăng dần
    unique_sorted_list = sorted(unique_set)
    return unique_sorted_list

# Ví dụ sử dụng:
a = [1, 5, 3, 7, 5, 9, 7]
b = Duynhat(a)
print("Mảng b chứa các số duy nhất có trong mảng a và có thứ tự tăng dần:", b)  # Kết quả mong đợi: [1, 3, 5, 7, 9]





### bài 2
def Hieu(a, b):
    # Sử dụng tập hợp để lấy các số không trùng nhau có trong a nhưng không có trong b
    difference_set = set(a) - set(b)
    # Sắp xếp các số trong tập hợp để có thứ tự tăng dần
    difference_sorted_list = sorted(difference_set)
    return difference_sorted_list

# Ví dụ sử dụng:
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
c = Hieu(a, b)
print("Mảng c chứa các số không trùng nhau có trong mảng a nhưng không có trong mảng b và có thứ tự tăng dần:", c)
# Kết quả mong đợi: [1, 4, 5, 7]





### bài 3
def Giao(a, b):
    # Sử dụng tập hợp để lấy các số trùng nhau có trong cả a và b
    intersection_set = set(a) & set(b)
    # Sắp xếp các số trong tập hợp để có thứ tự tăng dần
    intersection_sorted_list = sorted(intersection_set)
    return intersection_sorted_list

# Ví dụ sử dụng:
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
c = Giao(a, b)
print("Mảng c chứa các số đồng thời có trong mảng a và mảng b và có thứ tự tăng dần:", c)
# Kết quả mong đợi: [3, 9]




### bài 4
def Hop(a, b):
    # Sử dụng tập hợp để lấy các số không trùng nhau có trong cả a và b
    union_set = set(a) | set(b)
    # Sắp xếp các số trong tập hợp để có thứ tự tăng dần
    union_sorted_list = sorted(union_set)
    return union_sorted_list

# Ví dụ sử dụng:
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
c = Hop(a, b)
print("Mảng c chứa các số có trong mảng a và / hoặc mảng b và có thứ tự tăng dần:", c)
# Kết quả mong đợi: [1, 2, 3, 4, 5, 6, 7, 8, 9]

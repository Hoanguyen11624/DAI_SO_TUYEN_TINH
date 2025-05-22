import numpy as np

# Khai báo ma trận M1
print("=== KHAI BÁO MA TRẬN ===")
M1 = np.array([[9, 12], [23, 30]])
print("Ma trận M1:")
print(M1)
print("Kết quả hiển thị:")
print("[[ 9 12]")
print(" [23 30]]")

print("\n" + "="*50)

# Khai báo vector u
print("=== KHAI BÁO VECTOR ===")
u = np.array([2, 1])
print("Vector u:", u)

print("\n" + "="*50)

# Phép tích M1.dot(u) - Ma trận nhân vector
print("=== PHÉP TÍCH M1.dot(u) ===")
tichM1u = M1.dot(u)
print("tichM1u = M1.dot(u)")
print("Kết quả:", tichM1u)
print("\nGiải thích:")
print("Đây là phép nhân ma trận (2x2) với vector cột (2x1)")
print("M1 * u = [[9, 12], [23, 30]] * [[2], [1]]")
print("Kết quả:")
print("- Hàng 1: 9*2 + 12*1 = 18 + 12 = 30")
print("- Hàng 2: 23*2 + 30*1 = 46 + 30 = 76")
print("=> Vector kết quả: [30, 76]")

print("\n" + "="*50)

# Phép tích u.dot(M1) - Vector nhân ma trận
print("=== PHÉP TÍCH u.dot(M1) ===")
tichuM1 = u.dot(M1)
print("tichuM1 = u.dot(M1)")
print("Kết quả:", tichuM1)
print("\nGiải thích:")
print("Đây là phép nhân vector hàng (1x2) với ma trận (2x2)")
print("u * M1 = [2, 1] * [[9, 12], [23, 30]]")
print("Kết quả:")
print("- Cột 1: 2*9 + 1*23 = 18 + 23 = 41")
print("- Cột 2: 2*12 + 1*30 = 24 + 30 = 54")
print("=> Vector kết quả: [41, 54]")

print("\n" + "="*50)

# Sử dụng np.dot(M1, u)
print("=== PHÉP TÍCH np.dot(M1, u) ===")
result1 = np.dot(M1, u)
print("np.dot(M1, u) =", result1)
print("\nGiải thích:")
print("Kết quả giống với M1.dot(u)")
print("Đây là phép nhân ma trận với vector cột")
print("Kết quả: [30, 76]")

print("\n" + "="*50)

# Sử dụng np.dot(u, M1)
print("=== PHÉP TÍCH np.dot(u, M1) ===")
result2 = np.dot(u, M1)
print("np.dot(u, M1) =", result2)
print("\nGiải thích:")
print("Kết quả giống với u.dot(M1)")
print("Đây là phép nhân vector hàng với ma trận")
print("Kết quả: [41, 54]")

print("\n" + "="*50)

# Tổng kết
print("=== TỔNG KẾT ===")
print("1. M1.dot(u) = np.dot(M1, u) = [30, 76] (ma trận × vector cột)")
print("2. u.dot(M1) = np.dot(u, M1) = [41, 54] (vector hàng × ma trận)")
print("\nSự khác biệt:")
print("- Thứ tự của phép nhân rất quan trọng trong đại số tuyến tính")
print("- Kích thước kết quả có thể khác nhau")
print("- Ý nghĩa hình học và toán học khác nhau")
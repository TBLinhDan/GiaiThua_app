# Bài toán Tính Giai Thừa bằng phương pháp Đệ quy: Hàm gọi lại chính nó trong câu lệnh của Hàm
def fact(n):
  if n == 0 or n ==1:
    return 1
  else:
    return n*fact(n-1)
  
print(fact(6))
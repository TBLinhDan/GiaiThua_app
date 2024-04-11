import streamlit as st
from giaithua import fact

def main():
  st.title("TOÁN GIAI THỪA")
  number = st.number_input("Nhập Số Nguyên dương", min_value =0, max_value =900)

  if st.button("Tính Toán"):
    result = fact(number) # Gọi hàm fact() từ file factorial.ny đã import
    st.write(f"{number} giai thừa ({number}!) có giá trị: {result}")
    st.balloons()

if __name__ == "__main__":
  main()
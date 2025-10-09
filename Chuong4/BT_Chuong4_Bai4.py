 # Câu 4: Viết Hàm Tính ROI

def ROI(dt, cp):
    return (dt - cp) / cp

def GoiYDauTu(roi):
    if roi >= 0.75:
        return "Nên đầu tư"
    else:
        return "Không nên đầu tư"

print("Chương trình tính ROI")
dt = int(input("Nhập Doanh Thu: "))
cp = int(input("Nhập chi phí: "))
if cp == 0:
    print("Chi phí phải khác 0!")
else:
    roi = ROI(dt, cp)
    print("Tỉ Lệ ROI =", round(roi, 2))
    print("==>", GoiYDauTu(roi))
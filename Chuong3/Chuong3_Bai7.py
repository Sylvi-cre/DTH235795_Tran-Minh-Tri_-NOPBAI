def kiemTraNamNhuan(nam):
    if (nam % 4 ==0 and nam % 100 != 0) or nam % 400 == 0:
        print("Năm ", nam, " là năm nhuần")
        return 1
    else:
        print("Năm ", nam, " không nhuần")
        return 0

def NgayKeTiep(ngay, thang, nam):   

    if thang in (1, 3, 5, 7, 8, 10, 12):
        max_day = 31
    elif thang in (4, 6, 9, 11):
        max_day = 30
    elif thang == 2:
        if (kiemTraNamNhuan(nam) == 1):
            max_day = 29
        else:
            max_day = 28
    else:
        return None
    if ngay < 1 or ngay > max_day:
        return None 
    if ngay < max_day:
        return ngay + 1, thang, nam
    else:  
        if thang == 12:
            return 1, 1, nam + 1
        else:
            return 1, thang + 1, nam
# main
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
dmy = NgayKeTiep(ngay, thang, nam)
if dmy is None:
    print("Ngày không hợp lệ!")
else:
    d, m, y = dmy
    print(f"Ngày kế tiếp là: {d}/{m}/{y}")

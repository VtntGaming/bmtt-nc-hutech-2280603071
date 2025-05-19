def chiaHet5(soNhiPhan):
    soThapPhan = int(soNhiPhan,2)
    return soThapPhan%5==0
chuoiNhiPhan = input("Nhập chuỗi số nhị phân (phân tách bởi dấu phẩy):")

dsSoNhiPhan = chuoiNhiPhan.split(',')
dsChiaHet5 = [so for so in dsSoNhiPhan if chiaHet5(so)]
if len(dsChiaHet5)>0:
    kq = ','.join(dsChiaHet5)
    print("Các số nhị phân chia hết cho 5:",kq)
else:
    print("Không có số nào chia hết cho 5")
    
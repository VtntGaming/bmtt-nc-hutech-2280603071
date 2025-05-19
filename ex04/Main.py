from QuanLySV import QuanLySinhVien

qlsv = QuanLySinhVien()

while True:
    print("\nCHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
    print("**************************MENU**************************")
    print("** 1. Thêm sinh viên.")
    print("** 2. Cập nhật thông tin sinh viên.")
    print("** 3. Xoá sinh viên.")
    print("** 4. Tìm kiểm sinh viên theo tên.")
    print("** 5. Tìm kiểm sinh viên theo ĐTB.")
    print("** 6. Tìm kiểm sinh viên theo tên chuyên ngành.")
    print("** 7. Hiển thị danh sách sinh viên.")
    print("** 0. Thoát.")
    print("********************************************************")

    key = int(input("Lựa chọn:"))
    if key==1:
        qlsv.nhapSV()
        print("Nhập thông tin sinh viên thành công!")
    elif key == 2:
        if qlsv.soLuongSV() > 0:
            print("Nhập ID: ")
            ID = int(input())
            qlsv.updateSV(ID)
        else:
            print("DS sinh viên đang trống!")
    elif (key == 3):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n3. Xóa sinh viên.")
            print("\nNhập ID: ")
            ID = int(input())
            if (qlsv.deleteById(ID)):
                print("\nSinh vien có id=", ID, "đã bị xóa.")
            else:
                print("\nSinh vien co id = ", ID," khong ton tal.")
        else:
            print("\nDS sinh viên đang trống!")
    elif (key == 4):
        if (qlsv.soLuongSinhVien() > 0):
            print("\nNhập sv cần tìm kiếm: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSV(searchResult)
    elif (key == 5):
        if (qlsv.soluongSinhVien() > 0):
            qlsv.sortByDTB()
            qlsv.showSV(qlsv.getDsSinhVien())
        else:
            print("\nDanh sách sinh viên đang trống!")
    elif (key == 6):
        if (qlsv.soluongSinhVien() > 0):
            print("\n6. Sap xep sinh vien theo ten.")
            qlsv.sortByName()
            qlsv.showSV(qlsv.getDsSinhVien())
        else:
            print("\nDanh sách sinh viên đang trống!")
    elif (key == 7):
        if (qlsv.soLuongSV() > 0):
            qlsv.showSV(qlsv.getDsSinhVien())
        else:
            print("\nDanh sách sinh viên đang trống!")
    elif (key == 0):
        print("\n Chương trình kết thúc!")
        break
    else:
        print("\n Không có chức năng này, hãy chon chuc nang trong hop menu.")
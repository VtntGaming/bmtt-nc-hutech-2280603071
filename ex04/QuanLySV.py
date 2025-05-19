from SinhVien import SinhVien

class QuanLySinhVien:
    dsSinhVien = []

    def generateID(self):
        maxId = 1
        if self.soLuongSV() > 0:
            maxId = self.dsSinhVien[0]._id
            for sv in self.dsSinhVien:
                if (maxId < sv._id):
                    maxId = sv._id
            maxId = maxId + 1
        return maxId

    def soLuongSV(self):
        return self.dsSinhVien.__len__()
    
    def nhapSV(self):
        id = self.generateID()
        name = input("Nhập tên sv: ")
        sex = input("Nhập giới tính: ")
        major = input("Nhập chuyên ngành: ")
        dtb = input("Nhập điểm: ")
        sv = SinhVien(id, name, sex, major, float(dtb))
        self.xepLoaiHocLuc(sv)
        self.dsSinhVien.append(sv)

    def updateSV(self, ID):
        sv:SinhVien = self.findByID(ID)
        if (sv != None):
            name = input("Nhập tên sv: ")
            sex = input("Nhập giới tính: ")
            major = input("Nhập chuyên ngành: ")
            dtb = input("Nhập điểm: ")
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._dtb = float(dtb)
            self.XepLoaiHocLuc(sv)
        else:
            print(f"Sinh viên có id = {ID} không tồn tại!")

    def sortByID(self):
        self.dsSinhVien.sort(key=lambda x:x._id, reverse=False)

    def sortByName(self):
        self.dsSinhVien.sort(key=lambda x:x._name, reverse=False)

    def sortByDTB(self):
        self.dsSinhVien.sort(key=lambda x:x._dtb, reverse=False)\
        
    def findByID(self, id):
        if (self.soLuongSV()>0):
            for sv in self.dsSinhVien:
                if (sv._id==id):
                    return sv
        return None
    
    def findByName(self, name):
        if (self.soLuongSV()>0):
            for sv in self.dsSinhVien:
                if (sv._name==name):
                    return sv
        return None
    
    def deleteByID(self, id):
        sv = self.findByID(id)
        if (sv!=None):
            self.dsSinhVien.remove(sv)
            return True
        else:
            return False
    
    def xepLoaiHocLuc(self, sv:SinhVien):
        if sv._dtb>=8: sv._hocluc = "Giỏi"
        elif sv._dtb>=6.5: sv._hocluc = "Khá"
        elif sv._dtb>=5: sv._hocluc = "Trung bình"
        else: sv._hocluc = "Yếu"

    def showSV(self, danhSachSV):
        print("{:<18}{:<18}{:<18}{:<32}{:<18}{:<18}".format("ID","Tên","Giới tính", "Chuyên ngành", "DTB", "Học lực"))

        if danhSachSV.__len__()>0:
            for sv in danhSachSV:
                print("{:<18}{:<18}{:<18}{:<32}{:<18}{:<18}".format(sv._id, sv._name,sv._sex,sv._major,sv._dtb,sv._hocluc))
            print("\n")

    def getDsSinhVien(self):
        return self.dsSinhVien
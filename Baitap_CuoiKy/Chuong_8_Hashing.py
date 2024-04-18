### bài 1
class TuDien:
    def __init__(self):
        # Khởi tạo một từ điển rỗng
        self.tu_dong_nghia = {}
        self.tu_trai_nghia = {}

    def NhapTu(self, tu, dong_nghia=None, trai_nghia=None):
        # Lấy ký tự đầu tiên của từ làm khóa cho từ điển
        khoa = tu[0].lower()
        
        # Thêm từ vào từ điển đồng nghĩa nếu có
        if dong_nghia:
            # Nếu chưa có từ khóa trong từ điển, tạo một danh sách mới
            if khoa not in self.tu_dong_nghia:
                self.tu_dong_nghia[khoa] = []
            # Thêm từ đồng nghĩa vào danh sách
            self.tu_dong_nghia[khoa].append(dong_nghia)
        
        # Thêm từ vào từ điển trái nghĩa nếu có
        if trai_nghia:
            # Nếu chưa có từ khóa trong từ điển, tạo một danh sách mới
            if khoa not in self.tu_trai_nghia:
                self.tu_trai_nghia[khoa] = []
            # Thêm từ trái nghĩa vào danh sách
            self.tu_trai_nghia[khoa].append(trai_nghia)

    def TraTu(self, tu):
        khoa = tu[0].lower()
        dong_nghia = self.tu_dong_nghia.get(khoa, [])
        trai_nghia = self.tu_trai_nghia.get(khoa, [])
        return dong_nghia, trai_nghia

# Ví dụ sử dụng
td = TuDien()
td.NhapTu("mèo", "con mèo", "chó")
td.NhapTu("chó", "con chó", "mèo")
td.NhapTu("vui", "hạnh phúc", "buồn")

tu_can_tra = "mèo"
dong_nghia, trai_nghia = td.TraTu(tu_can_tra)
print(f"Từ đồng nghĩa của '{tu_can_tra}' là: {dong_nghia}")
print(f"Từ trái nghĩa của '{tu_can_tra}' là: {trai_nghia}")





### bài 2
class TuDien:
    def __init__(self):
        # Khởi tạo một từ điển rỗng
        self.tu_dong_nghia = {}
        self.tu_trai_nghia = {}

    def NhapTu(self, tu, dong_nghia=None, trai_nghia=None):
        # Lấy ký tự đầu tiên của từ làm khóa cho từ điển
        khoa = tu[0].lower()
        
        # Thêm từ vào từ điển đồng nghĩa nếu có
        if dong_nghia:
            # Nếu chưa có từ khóa trong từ điển, tạo một danh sách mới
            if khoa not in self.tu_dong_nghia:
                self.tu_dong_nghia[khoa] = []
            # Thêm từ đồng nghĩa vào danh sách
            self.tu_dong_nghia[khoa].extend(dong_nghia)
        
        # Thêm từ vào từ điển trái nghĩa nếu có
        if trai_nghia:
            # Nếu chưa có từ khóa trong từ điển, tạo một danh sách mới
            if khoa not in self.tu_trai_nghia:
                self.tu_trai_nghia[khoa] = []
            # Thêm từ trái nghĩa vào danh sách
            self.tu_trai_nghia[khoa].extend(trai_nghia)

    def DongNghia(self, tu):
        khoa = tu[0].lower()
        dong_nghia = self.tu_dong_nghia.get(khoa, [])
        return dong_nghia

    def TraiNghia(self, tu):
        khoa = tu[0].lower()
        trai_nghia = self.tu_trai_nghia.get(khoa, [])
        return trai_nghia

# Ví dụ sử dụng
td = TuDien()
td.NhapTu("mèo", ["con mèo", "gàu gàu"], ["chó", "hổ"])
td.NhapTu("chó", ["con chó"], ["mèo"])
td.NhapTu("vui", ["hạnh phúc"], ["buồn"])

tu_can_tra = "mèo"
dong_nghia = td.DongNghia(tu_can_tra)
trai_nghia = td.TraiNghia(tu_can_tra)
print(f"Từ đồng nghĩa của '{tu_can_tra}' là: {dong_nghia}")
print(f"Từ trái nghĩa của '{tu_can_tra}' là: {trai_nghia}")





### bài 3
class Album:
    def __init__(self, ten_album, danh_sach_bai_hat):
        self.ten_album = ten_album
        self.danh_sach_bai_hat = danh_sach_bai_hat

    def hien_thi(self):
        print(f"Album: {self.ten_album}")
        print("Danh sách bài hát:")
        for bai_hat in self.danh_sach_bai_hat:
            print(f"  - Tên bài hát: {bai_hat['ten_bai_hat']}")
            print(f"    + Nhạc sĩ: {bai_hat['nhac_si']}")
            print(f"    + Ca sĩ: {bai_hat['ca_si']}")
        print("\n")

class TuDien:
    def __init__(self):
        self.albums = {}

    def NhapAlbum(self, ten_album, danh_sach_bai_hat):
        album = Album(ten_album, danh_sach_bai_hat)
        self.albums[ten_album] = album

    def XemAlbum(self, ten):
        album = self.albums.get(ten)
        if album:
            album.hien_thi()
        else:
            print(f"Không tìm thấy album có tên '{ten}'")

# Ví dụ sử dụng
td = TuDien()
td.NhapAlbum("Album A", [
    {"ten_bai_hat": "Bài hát 1", "nhac_si": "Nhạc sĩ A", "ca_si": "Ca sĩ X"},
    {"ten_bai_hat": "Bài hát 2", "nhac_si": "Nhạc sĩ B", "ca_si": "Ca sĩ Y"}
])
td.NhapAlbum("Album B", [
    {"ten_bai_hat": "Bài hát 3", "nhac_si": "Nhạc sĩ C", "ca_si": "Ca sĩ Z"},
    {"ten_bai_hat": "Bài hát 4", "nhac_si": "Nhạc sĩ D", "ca_si": "Ca sĩ W"}
])

td.XemAlbum("Album A")
td.XemAlbum("Album C")  # Album không tồn tại

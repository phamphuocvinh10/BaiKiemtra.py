import Service

filename = "bt2.txt"

check = -1
while check != 0 or check.isnumeric() is False:
    print("1. Đọc file")
    print("2. Tạo file dữ liệu ngẫu nhiên")
    print("3. Liệt kê hình có chu vi, diện tích lớn nhất")
    print("4. Kiểm tra số lượng hình nằm chồng lên nhau nhiều nhất ")
    print("5. Hiển thị danh sách hình ")
    check = input("Nhập mã lệnh:")
    while check.isnumeric() is False or int(check) < 0 or int(check) > 5:
        check = input("Nhập lại mã lệnh")
    check = int(check)
    if check == 1:
        rs = False
        while rs is False:
            filename = str(input("Nhập tên file:")) + ".txt"
            rs = Service.readfile(filename)
    elif check == 2:
        rs = False
        while rs is False:
            filename = str(input("Nhập tên file:")) + ".txt"
            amount = int(input("Nhập số lượng:"))
            rs = Service.createfile(filename, amount)
    elif check == 3:
        Service.checkmax()
    elif check == 4:
        Service.maxcollide()
    elif check == 5:
        e=0
        while e<=0 or e>3:
            print("1. Danh sách hình vuông")
            print("2. Danh sách hình tròn")
            print("3. Danh sách hình tam giác")
            e = int(input("Nhập số:"))
            Service.getinfo(e)
    elif check == 0:
        break

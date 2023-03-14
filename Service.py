import random
from Class import Triangle, Rect, Circle
rec = []
tri = []
cir = []


def generateRec(f):
    a = random.randint(0, 20)
    b = random.randint(0, 20)
    if a > b:
        c = a
        a = b
        b = c
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    f.write("#Rect\n")
    f.write("{} {}\n".format(a, b))
    f.write("{} {}\n".format(x, y))


def generateCir(f):
    bk = random.randint(0, 10)
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    f.write("#Circle\n")
    f.write("{}\n".format(bk))
    f.write("{} {}\n".format(x, y))


def generateTri(f):
    a, b, c = 0, 0, 0
    while a + b <= c or a + c <= b or \
            b + c <= a:
        a = random.randint(0, 20)
        b = random.randint(0, 20)
        c = random.randint(0, a + b)
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    f.write("#Triangle\n")
    f.write("{} {} {}\n".format(a, b, c))
    f.write("{} {}\n".format(x, y))

#Bài 1
def createfile(filename="input.txt", amount=1000):
    try:
        with open(filename, "w") as f:
            for i in range(amount):
                generateRec(f)
                generateCir(f)
                generateTri(f)
        return True
    except:
        return False

# Bài 4a
def readfile(filename):
    global rec
    global cir
    global tri
    try:
        with open(filename) as file:
            line = file.readline()
            while line != '':
                if line == "#Rect\n":
                    data = file.readline()
                    data.replace("\n", "")
                    info = [int(x) for x in data.split(" ")]
                    data2 = file.readline()
                    data2.replace("\n", "")
                    info2 = [int(x) for x in data2.split(" ")]
                    rect = Rect(info[0], info[1], info2[0], info2[1])
                    rec.append(rect)
                if line == "#Circle\n":
                    data = file.readline()
                    data.replace("\n", "")
                    info = int(data.strip())
                    data2 = file.readline()
                    data2.replace("\n", "")
                    info2 = [int(x) for x in data2.split(" ")]
                    circle = Circle(info, info2[0], info2[1])
                    cir.append(circle)
                if line == "#Triangle\n":
                    data = file.readline()
                    data.replace("\n", "")
                    info = [int(x) for x in data.split(" ")]
                    data2 = file.readline()
                    data2.replace("\n", "")
                    info2 = [int(x) for x in data2.split(" ")]
                    triangle = Triangle(info[0], info[1], info[2], info2[0], info2[1])
                    tri.append(triangle)
                line = file.readline()
        return True
    except:
        return False

# Bài 4b
def checkmax():
    maxCV = 0
    maxDT = 0
    for i in rec:
        if i.ChuVi > maxCV:
            cv = i
            maxCV = i.ChuVi
            print(maxCV)
        if i.DienTich > maxDT:
            dt = i
            maxDT = i.DienTich
            print(maxDT)
    for i in cir:
        if i.ChuVi > maxCV:
            cv = i
            maxCV = i.ChuVi
            print(maxCV)
        if i.DienTich > maxDT:
            dt = i
            maxDT = i.DienTich
            print(maxDT)
    for i in tri:
        if i.ChuVi > maxCV:
            cv = i
            maxCV = i.ChuVi
            print(maxCV)
        if i.DienTich > maxDT:
            dt = i
            maxDT = i.DienTich
            print(maxDT)
    print("Hình có chu vi lớn nhất với chu vi là {}:".format(maxCV))
    cv.printinfo()
    print("-"*30)
    print("Hình có diện tích lớn nhất với diện tích là {}:".format(maxDT))
    dt.printinfo()

from abc import ABC, abstractmethod
import math

#Bài 2
class Shape:
    @abstractmethod
    def printinfo(self):
        pass

    @abstractmethod
    def chuVi(self):
        pass

    @abstractmethod
    def dienTich(self):
        pass

#Bài 3
class Rect(Shape):
    def __init__(self, rong, dai, x, y, ):
        self.Rong = rong
        self.Dai = dai
        self.X = x
        self.Y = y
        self.ChuVi = self.chuVi()
        self.DienTich = self.dienTich()

    def printinfo(self):
        print("#Rectangle")
        print("Chiều rộng:{} Chiều dài:{}".format(self.Rong, self.Dai))
        print("Tọa độ: ({}, {})".format(self.X, self.Y))

    def chuVi(self):
        ChuVi = (self.Rong + self.Dai) * 2
        return ChuVi

    def dienTich(self):
        DienTich = self.Rong * self.Dai
        return DienTich


class Circle(Shape):
    def __init__(self, bk, x, y, ):
        self.BK = bk
        self.X = x
        self.Y = y
        self.ChuVi = self.chuVi()
        self.DienTich = self.dienTich()

    def printinfo(self):
        print("#Circle")
        print("Bán kính:{}".format(self.BK))
        print("Tọa độ: ({}, {})".format(self.X, self.Y))

    def chuVi(self):
        ChuVi = self.BK * 2 * 3.14
        return ChuVi

    def dienTich(self):
        DienTich = pow(self.BK, 2) * 3.14
        return DienTich


class Triangle(Shape):
    def __init__(self, a, b, c, x, y, ):
        self.A = a
        self.B = b
        self.C = c
        self.X = x
        self.Y = y
        self.ChuVi = self.chuVi()
        self.DienTich = self.dienTich()

    def printinfo(self):
        print("#Triangle")
        print("Cạnh A:{} Cạnh B:{} Cạnh C:{}".format(self.A, self.B, self.C))
        print("Tọa độ: ({}, {})".format(self.X, self.Y))

    def chuVi(self):
        ChuVi = self.A + self.B + self.C
        return ChuVi

    def dienTich(self):
        p = self.ChuVi / 2
        DienTich = math.sqrt(p * (p - self.A) * (p - self.B) * (p - self.C))
        return DienTich

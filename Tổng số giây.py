# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:18:46 2024

@author: NguyenNgocNhuQuynh
"""

gio = int(input("Nhập giờ: "))
phut = int(input("Nhập phút: "))
gi = int(input("Nhập giây: "))
tong_giay = gio * 3600 + phut * 60 + gi
print("Tổng số giây là: ",tong_giay)
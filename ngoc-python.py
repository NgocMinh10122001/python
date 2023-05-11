second = int(input("nhap vao: "))
#print(second)
day = second//(3600*24)
hour = (second-day*3600*24)//3600
minute = (second-day*3600*24-hour*3600)//60
second2 = second-day*3600*24-hour*3600- minute*60
print(second, 'giay =', day, 'ngay', hour, 'gio', minute, 'phut', second2, 'giay')
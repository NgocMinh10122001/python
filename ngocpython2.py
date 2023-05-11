price = int(input('gia ve thang: '))
name = input('ho ten: ')
age = int(input('tuoi: '))
months = int(input('so thang: '))
discount = 0
if (age <= 18):
    print('ban duoc mien giam 10%')
    discount = 0.1
else:
    if (age >= 60):
        print('ban duoc mien phi toan bo')
        discount = 1
    else:
        print('ban khong duoc mien giam')
value = months * price * (1-discount)
print('so tien phai tra: ', value)
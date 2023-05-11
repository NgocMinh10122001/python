a=float(input())
b=float(input())
c=float(input())
delta = b*b - 4*a*c
if a==0:
    if b==0:
        if c==0:
            print('Phuong trinh co vo so nghiem!')
        else:
            print('Phuong trinh vo nghiem!')
    else:
        if c==0:
            print('Phuong trinh vo nghiem!')
        else:
            x = -c/b
            print('Phuong trinh co mot nghiem: x =',f'{x:.3f}')
            
else:
    if delta<0:
        print('Phuong trinh vo nghiem!')
    if delta==0:
        x3 =-b/(2*a)
        print('Phuong trinh co nghiem kep: x1 = x2 =',f'{x3:.3f}' )
    if delta>0:
        import math
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)
        print('Phuong trinh co 2 nghiem: x1 =', f'{x1:.3f}', 'va x2 =', f'{x2:.3f}')
    
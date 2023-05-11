def nhap_du_lieu():
    a=float(input())
    b=float(input())
    return a, b
def phuong_trinh_vo_nghiem():
    print ('phuong trinh vo nghiem')
def phuong_trinh_vo_so_nghiem():
    print ('phuong trinh vo so nghiem')
def phuong_trinh_co_nghiem():
    x=-b/a
    print ('phuong trinh co nghiem: x=', x)
a, b = nhap_du_lieu()
if a==0:
    if b==0:
        phuong_trinh_vo_so_nghiem()
    else:
        phuong_trinh_vo_nghiem()
else:
    phuong_trinh_co_nghiem()
    
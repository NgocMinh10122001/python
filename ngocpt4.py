def kiem_tra_so_nguyen_to(n):
    count=0
    for i in range(1,n+1):
        if n%i == 0:
            count=count+1
    if count == 2:
        return True
    return False
n = int(input())
print(kiem_tra_so_nguyen_to(n))
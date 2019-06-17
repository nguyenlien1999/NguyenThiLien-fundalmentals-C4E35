import math
print("moi ban nhap vao thong tin hinh tron ")
r=int(input(r))
if(r<=0):
    print("mời bạn nhập lại bán kính,bán kính phải lớn hơn 0")
else:
    print("moi ban nhap vao ban kinh", r)
    chuvi=(2*math.pi*r)
    print("chu vi hinh tron  ",chuvi)
    dientich= (r*r*math.pi)
    print("dien tich hình tron",dientich)


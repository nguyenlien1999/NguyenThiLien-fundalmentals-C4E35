ns=int (input("moi ban nhap vao nam sinh"))
namht=int (input(namht))
print("moi ban nhap vap nam hien tai",namht)
tuoi=namht-ns+1
print("tuoi cua ban la",tuoi)
if tuoi<12 :
   print("tre em")
elif tuoi<=18:
    print("teen")
else:
    print("trưởng thành")

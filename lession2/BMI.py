print("tính chỉ số BMI (Chỉ số khối cơ thể)")
    height =float input(height)
print("Mời bạn nhập vào chiều cao theo đơn vị cm",height)
print("Đây là chiều cao tính theo đơn vị chuẩn m",height/100)
    weight =float input(weight)
print("Mời bạn nhập vào cân nặng theo đơn vị chuẩn kg",weight)
    BMI= (float)weight/(height*height)
print("Kết quả chỉ số BMI của người này là:",BMI)

if(BMI<16)  
    print("Thiếu cân nặng")
elif(BMI>=16 && BMI<18,5)
    print("Thiếu cân")
elif(BMI>=18,5 && BMI<25)
    print("Bình thường")
elif(BMI>=25 && BMI<30)
    print("Thừa cân")
else
     print("Béo phì")
return
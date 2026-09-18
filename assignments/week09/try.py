#error(buge)
#3 types = 1.syntax error ผิดไวยากรณ์
#          2.runtime error เกิดในจังหวะrun
#          3.logic error ผลลัพธ์ไม่ตรงกับที่คาดหวัง
age = int(input("your age "))
#Valueerror
try:
    print(age)
    #ลองทำในนี้

except ValueError:

    print("เขียนตัวเลข")
    #ถ้ามันerrorจะทำในนี้

#การหารเลขด้วย0
try:
    n = float(input("ตัวตั้ง  "))
    d = float(input("ตัวหาร "))
except  ValueError:
    print("กรุณากรอกตัวเลข")
except ZeroDivisionError :
    print("ตัวเลขไม่สามารถหารด้วยศูนย์ได้ ")

#error openfile , เปิดพร้อมสิทธิที่ไม่ได้รับอนุญาตขออ่านหรือเขียน error
except FileNotFoundError :
except PermissionError :

#raise คือคำสั่งยกว่าให้errorตามที่เราต้องการให้มันerrorถึงมันจะไม่errorตามหลัก
#else ใน try คือถ้าในtryปกติดีให้มาทำในelse
#finally คือจะแสดงผลไม่ว่าจะมีerror หรือไม่ก็ตาม


def calculate_electrivity_cost(user):
    kafai = int(input("หน่วยไฟฟ้า: "))
    if user == 1:
        if kafai > 1 and kafai < 51 :
            total = kafai * 2.5 
            print("รายละเอียดค่าไฟ")
            print(f"1-{kafai} หน่วย = ราคา{total}")
            print("ค่าบริการ 25 บาท")
            print(f"รวมทั้งสิ้น ",total +25)
        elif kafai > 50 and kafai < 101 :
            value = (kafai - 50)
            total = (value * 3.00 ) +125 +25
            print("รายละเอียดค่าไฟ")
            print(f"1 - 50 หน่วย = ราคา 125")
            print(f"51 - {kafai} หน่วย = ราคา{total} ")
            print("ค่าบริการ 25 บาท")
            print(f"รวมทั้งสิ้น ",total +25)
            
        elif kafai >100 and kafai < 201:
            value = (kafai - 100)
            total = (value * 3.50) + 125 + 150 +25
            print("รายละเอียดค่าไฟ")
            print(f"1 - 50 หน่วย = ราคา 125")
            print(f"51 - 100 หน่วย = ราคา 150 ")
            print(f"101 - {kafai}= ราคา {total}")
            print("ค่าบริการ 25 บาท")
            print(f"รวมทั้งสิ้น ",total +25)
        elif kafai >200 :
            value = (kafai - 200)
            total = (value *4.00)+125 +150 + 350 +25
            print("รายละเอียดค่าไฟ")
            print(f"1 - 50 หน่วย = ราคา 125")
            print(f"51 - 100 หน่วย = ราคา 150 ")
            print(f"101 - 200 = ราคา 350")
            print(f"201 - {kafai} = ราคา {total}")
            print("ค่าบริการ 25 บาท")
            print(f"รวมทั้งสิ้น ",total +25)

    elif user == 2:
        print("ออกจากโปรแกรม ")

    else :
        print("เลือกเมนูไม่ถูกต้อง")

while True :
    user = int(input("เลือกเมนู \n 1 คำนวนค่าไฟ \n 2 ออกจากโปรแกรม \n เมนู :"))
    if user ==2 :
        print("ออกจากโปรแกรม ")
        break
    calculate_electrivity_cost(user)
    



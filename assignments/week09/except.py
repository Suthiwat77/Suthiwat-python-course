try:
    number1 = float(input("ตัวเลขที่ 1:"))
    number2 = float(input("ตัวเลขที่ 2:"))
    operator = (input("เครื่องหมาย(+,-,*,/) : "))

    if operator == "+":
        total = number1 + number2
    elif operator == "-":
        total = number1 - number2
    elif operator == "*":
        total = number1 * number2
    elif operator == "/":
        total = number1 / number2
    else :
        raise ValueError("เครื่องหมาย + - * / เท่านั้น")

    print(f"{number1}{operator}{number2} = ",total)
except ValueError :
    print("ใส่ตัวเลขเท่านั้น !!!")

except ZeroDivisionError:
    print("ไม่สามารถหารด้วย0ได้")
finally :
    print("จบการทำงาน")

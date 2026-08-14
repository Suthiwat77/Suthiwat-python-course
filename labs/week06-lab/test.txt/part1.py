def calculate_rectangle_area(length, width):
    """Calculates and displays rectangle area"""
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} × {width} = {area}")
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)



def calculate_sarmlium_area(hight,base):
    area = hight * base * 0.5
    print(f"hight = {hight} and base = {base}")
    print(f"arae = {area}")
    print()

print("Calculating sarmlium areas:")
calculate_sarmlium_area(8, 3)
calculate_sarmlium_area(85, 5)


#สร้างfucntionคำนวณวงกลม

def calculate_vongglom_area(r):
    area = 3.14 * r**2
    print(f"redius = {r}")
    print(f"arae = {area}")
    print()

print("Calculating vongglom areas:")
calculate_vongglom_area(6)
calculate_vongglom_area(8) 

def get_circle_info(radius):
    """Calculates circle area and circumference"""
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return area, circumference

print("Circle calculations:")
radius = 5
area, circumference = get_circle_info(radius)
print(f"Circle with radius {radius}:")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
print()

def square_root(n):
    return n **0.5


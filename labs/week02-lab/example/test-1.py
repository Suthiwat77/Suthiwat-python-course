print("1. Circle Calculator:")
print("   - Ask user for radius")
print("   - Calculate area (π * r²)")
print("   - Calculate circumference (2 * π * r)")
print("   - Use 3.14159 for π")
print()

radius = float(input("radius ="))

area = (3.14159 * radius **2)
print("area = ",area)

circumference =( 2* 3.14159 * radius )
print("circumference =",circumference)
"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""
<<<<<<< HEAD

class Rectangle:
    def __init__(self,length,width):
        self.__length = length 
        self.__width = width

    def getarea(self):
        print(f"area of {self.__length} length and {self.__width} width = {self.__lenght * self.__width}")

    def getparameter(self):
        print(f"area of {self.__length} length and {self.__width} width = { 2 * self.__lenght + self.__width}")

    def isSquare(self):
        return self.__length == self.__width
    
r = Rectangle(20,3)
print(r.getarea())
=======
    
>>>>>>> upstream/main

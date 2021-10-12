import math

class Rectangle:
  def __init__(self, width, height): 
    self.Width = width
    self.Height = height

  def __str__(self):
    return ("Rectangle(width=" + str(self.Width) + ", height=" + str(self.Height) + ")")

  def set_height(self, height):
    self.Height = height
  
  def set_width(self, width):
    self.Width = width

  def get_area(self):
    self.Area = self.Width * self.Height
    return self.Area

  def get_perimeter(self):
    self.Perimeter = 2*self.Width + 2* self.Height
    return self.Perimeter
  
  def get_diagonal(self): 
    self.Diagonal = (self.Width ** 2 + self.Height ** 2) ** 0.5
    return self.Diagonal
  
  def get_picture(self):
    if (self.Width > 50 or self.Height > 50):
      return "Too big for picture."
    else:
      strings = ""
      for i in range(self.Height):
        for j in range(self.Width):
          strings = strings + "*"
        strings = strings + "\n"
      return strings
      
  def get_amount_inside(self, shape):
    amount = math.floor(self.get_area() / shape.get_area())
    return amount 


class Square(Rectangle):
  def __init__(self, side):
    self.Side = side
    Rectangle.__init__(self,side,side)

  def __str__(self):
    return ("Square(side=" + str(self.Side) + ")" )    

  def set_side(self, side):
    self.__init__(side)

  def set_height(self, side):
    self.set_side(side)
  
  def set_width(self, side):
    self.set_side(side)
    
    

rect = Rectangle(3,6)
sq = Square(5)

rect.set_width(51)
rect.get_picture()

#bigRect = Rectangle(6,8)

#bigRect.get_picture()
#print (bigRect.get_diagonal())
#print (bigRect.get_amount_inside(Rectangle(2,2)))







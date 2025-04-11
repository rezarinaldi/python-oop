# OOP -> Object
# Object (Blueprint) -> properties and methods

class Handphone:
  # instance properties
  def __init__(self, brand):
    self.brand = brand
    self.is_active = False

  # methods
  def turn_on(self):
    self.is_active = True
    print(f"Handphone {self.brand} is turned on!")

  def turn_off(self):
    self.is_active = False
    print(f"Handphone {self.brand} is turned off!")

oppo = Handphone("Oppo")
iphone = Handphone("IPhone")
realme = Handphone("Realme")

print("Oppo: ", oppo.is_active)
print("IPhone: ", iphone.is_active)
print("Realme: ", realme.is_active)

realme.turn_on()

print("------------")
print("Oppo: ", oppo.is_active)
print("IPhone: ", iphone.is_active)
print("Realme: ", realme.is_active)
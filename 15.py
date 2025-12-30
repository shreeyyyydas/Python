# Base class


# Single Inheritance
class Dog:
    def cookies(self):
        print("Dog eats cookies")

class Cow(Dog):
    def grass(self):
        print("Cow eats grass")
# Multilevel Inheritance       
class Goat(Cow):
    def leaves(self):
        print("Goat eats leaves")
        
class Rabbit(Goat):
    def carrot(self):
        print("Rabbit eats carrot")
# --- Testing Single Inheritance ---
print("Single Inheritance")
 
cow = Cow()
cow.cookies()   
cow.grass()   
print("\nMultilevel Inheritance")
goat=Goat()
goat.cookies()   # Inherited from Dog
goat.grass()
goat.leaves()
print("\n")
rabbit=Rabbit()
rabbit.cookies()   # Inherited from Dog
rabbit.grass()
rabbit.leaves()
rabbit.carrot()





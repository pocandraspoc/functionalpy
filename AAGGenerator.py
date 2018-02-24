
import secrets
import string

class Car():
        """
        This CAR class represents a Bird, it has a name, a color, a size,
        and an x,y,z position.  This is a doc string for the class.  It's
        always good to include doc strings for classes and class methods.
        """
        def __init__(self, name, color, size):
            """
            This __init__ method is called when an instance of a Bird is
            constructed.  Pass the name, color, and size.
            """
            self.name = name
            self.color = color
            self.size = size
            self.x = 0
            self.y = 0
            self.z = 0
        def flyToLocation(self, x, y, z):
            """
            Update the x,y,z position of the bird.
            """
            self.x = x
            self.y = y
            self.z = z
'''
obj = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(self))
print(obj)
'''

randString = lambda self:''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(self))


carGenerator = (car for car in range(10))
'''
for car in carGenerator:
	carList[car]=Car(randString(2), randString(4), secrets.randbelow(10))
	print(carList[index].name)
'''
def gener(self):
	myList = range(self)
	for i in myList:
		yield i*i


myGener = gener(10)
for index in myGener:
	print(index)
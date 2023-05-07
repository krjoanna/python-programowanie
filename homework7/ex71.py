#Create a function find_axis(v1, v2) which returns the unit vector v3,
# where v3 is perpendicular to the vectors v1 and v2. 
#If the vectors v1 and v2 are parallel (or zero) then the function should raise an exception (ValueError) 
#[Hint: v1 and v2 are parallel if the cross product v1 × v2 is zero]. 
#Vectors are instances of the Vector class from Homework 6.

import math
class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):      # return string "Vector(x, y, z)"
        return "Vector ({}, {}, {})".format(self.x, self.y, self.z)
    
    def __eq__(self, other):    # v == w
        return self.x, self.y, self.z == other.x, other.y, other.z
    
    def __ne__(self, other):        # v != w
        return not self.x, self.y, self.z == other.x, other.y, other.z

    def __add__(self, other):   # v + w
        return Vector((self.x + other.x), (self.y + other.y), (self.z + other.z) )

    def __sub__(self, other):   # v - w
        return Vector((self.x - other.x), (self.y - other.y), (self.z - other.z))

    def __mul__(self, other):   #return the dot product (number)) 
        # a · b = a1 * b1 + a2 * b2 + a3 * b3
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):   # return the cross product (Vector)
        # a × b = (a2 * b3 - a3 * b2, a3 * b1 - a1 * b3, a1 * b2 - a2 * b1)
        return Vector((self.y * other.z - self.z * other.y), 
                      (self.z * other.x - self.x * other.z), 
                      (self.x * other.y - self.y * other.x))

    def length(self):   # the length of the vector
        return math.sqrt(self*self)

    def __hash__(self):   # we assume that vectors are immutable
        return hash((self.x, self.y, self.z))   # recommended

def find_axis(v1, v2):
    v3 = v1.cross(v2)     #wektor v3 prostopadły do v1 i v2
    v0 = Vector(0, 0, 0)
    if (v3.x, v3.y, v3.z) == (v0.x, v0.y, v0.z):
        raise ValueError("Vectors v1 & v2 are parallel")
    l = v3.length()
    v3 = v3.x/l,  v3.y/l, v3.z/l #v3 as unit vector
    return v3

#test
v1 = Vector(2, 6, 24)
v2 = Vector(3, 1, 2)
print(find_axis(v1,v2))



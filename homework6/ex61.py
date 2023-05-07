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

# Exemplary tests. Change values in your tests.
import math

v = Vector(2, 1, -1)
w = Vector(3, 1, 2)
#test1
assert v != w
assert v + w == Vector(5, 2, 1)
assert v - w == Vector(-1, 0, -3)
assert v * w == 5
# a × b = (a2 * b3 - a3 * b2, a3 * b1 - a1 * b3, a1 * b2 - a2 * b1)
assert v.cross(w) == Vector(3,-5 , -1)
assert v.length() == math.sqrt(6)
S = set([v, w])
assert len(S) == 2

#test2
assert v == v
assert v + v == Vector(4, 2, -2)
assert v - v == Vector(0, 0, 0)
assert v * v == 6
assert v.cross(v) == Vector(0, 0 , 0)
assert v.length() == math.sqrt(6)
S = set([v, v, v])
assert len(S) == 1

#test3
assert w == w
assert w + w == Vector(6, 2, 4)
assert w - w == Vector(0, 0, 0)
assert w * w == 14
assert w.cross(w) == Vector(0, 0, 0)
assert w.length() == math.sqrt(14)
S = set([w, w, w])
assert len(S) == 1

print("Tests passed")
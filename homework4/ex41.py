#Let p=(x,y) be a point in a plane. Define the following functions using lambda:
#(a) a test if p is in unit circle,
#(b) a test if the coordinates of p are positive,
#(c) a sorting key (y decreasing, x increasing),
#(d) a sorting key (the sum |x|+|y|).

#Using tests: list(filter((lambda p: ...), point_list))
#Using sorting keys: point_list.sort(key=lambda p: ...)


x = float(input("Enter x coordinate for point p in a plane: "))
y = float(input("Enter y coordinate for point p in a plane: "))

#### a) Unit Circle
TestUnitCircle = lambda x, y: x*x + y*y

if TestUnitCircle(x,y) == 1:
    print("a) p= ({},{}) is in unit circle".format(x,y))
else:
    print("a) p = ({},{}) is not in unit circle".format(x,y))

#### b) test positive
TestPositiveX = lambda x: x <=0 
TestPositiveY = lambda y: y <=0 

if TestPositiveX(x) == True or TestPositiveY(y) == True:
    print("b) For p= ({},{}) at least one coordinate is negative".format(x,y))
else:
    print("b) For p= ({},{}) coordinates are positive".format(x,y))


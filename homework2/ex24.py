#str
# (a) Find Unicode code points (int) for all characters of your name.
#Example: "Andrzej" --> [65, 110, 100, 114, 122, 101, 106]

YourName= "Joanna"

print("\nUnicode code points for name Joanna are: " 
      + str([ord(n) for n in YourName]))

################################################################################################
#(b) Prepare the periodic table (ten elements) as a list
pt = ((1,"Hydrogen","H",1), (2,"Helium","He",4), (3,"Lithium","Li",7), (4, "Beryllium","Be", 9), \
    (5, "Boron", "B", 11), (6, "Carbon", "C", 12), (7, "Nitrogen", "N", 14), (8, "Oxygen", "O", 16), \
    (9, "Fluorine", "F", 19), (10, "Neon", "Ne", 20))

print ("\n+---+--------------------+------+----------+",\
       "\n|{:<3}|{:<20}|{:<6}|{:<10}|".format('No.','Name (en)','Symbol','Weight (u)'),\
       "\n+---+--------------------+------+----------+")
for i in pt:
    a = i[0]
    b = i[1]
    c = i[2]
    d = i[3]
    print ("|{:>3}|{:<20}|{:^6}|{:>10}|".format(a, b, c, d))
print("+---+--------------------+------+----------+")
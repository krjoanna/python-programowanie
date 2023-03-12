#tuple
# Find and explain the results.

t = (2, 4)
print(t[2])             

#Elementy krotki są indeksowane rozpoczynająć od 0, a krotka t ma tylko 2 elementy. 
#Dlatego nie da się wydrukować elementu indeksowanego numerem 2. 
#(bo krotka nie posiada trzeciego elementu, który byłby indeksowany numerem 2).

t.append(6)

#krotki są niezmienialne, więc nie możemy dodać elementu 

a, b = t ; print(a, b)

#krotka została rozpakowana, do zmiennych a i b zostały dopasowane kolejne elementy krotki. 
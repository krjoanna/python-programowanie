
#Reversing a part of a list in place, reverse_range(L, left, right), the right index is included. Write iterative and recursive versions.
# Example.
#L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#reverse_range(L, 3, 6)   # index 6 is included!
#print(L)   # [0, 1, 2, 6, 5, 4, 3, 7, 8, 9]   # the list L changed
# The numbers outside the range are intact.

Lista = ["magda", "Helena", "Patrycja", "Weronika", "Asia", 5, 12, 0, 14]

def reverse_range(L, left, right):
    ListLenght = len (L)
    list_part = L[left:right]
    list_part.reverse()
    L = L[:left] + list_part + L[right:ListLenght]
    print(L)

reverse_range(Lista, 2, 6)



#bool
## Explain the results.
x = 5
x == 5 and 3       # 3    --> zwraca 3 (ostatni int), bo x jest równe 5
x == 4 and 3                # False --> zwraca False, bo x nie jest równe 4
3 and x == 5                  # True  --> zwraca True, bo x jest równy 5
3 and x == 4                  # False --> zwraca False, bo x nie jest równy 4

isinstance(True, int)         # True --> bo kiedyś true== 1 false == 0 , czyli są int (należy do podklasy int)
isinstance(True, bool)        # True --> True należy do klasy bool
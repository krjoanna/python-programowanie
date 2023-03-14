# For a given word (you may use your name), print it in squares.
# If word = "Python", them the result is
# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+

print("Podaj słowo, ktore chcesz wydrukowaś w kwadratach: ") 
a =input()

SignList = list(a)
ListLenght = len(SignList)

#pętla robiąca obramowanie tabeli
TableFrameList = list("+")
for i in range(0,ListLenght):
    TableFrameList.append("---+")
TableFrameString = ''.join(TableFrameList)

#pętla robiąca napis
WordRow = list("| ")
for i in SignList:
    WordRow.append(i)
    WordRow.append(" | ")
WordRowString = ''.join(WordRow)

print(TableFrameString)
print(WordRowString)
print(TableFrameString)
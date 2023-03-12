#list
#Let S be a long string (many lines).
#Find the number of black characters in S [not whitespace, see the method S.isspace()]. 
#Find the number of words in S (a word is a sequence of black characters).
#Find the longest word in S.
#Sort words from S according to (1) the lexicographic order, (2) the length.

S = "\nZ opisywaniem chmur \nmusiałabym się bardzo śpieszyć - \njuż po ułamku chwili \nprzestają być te, zaczynają być inne. \
    \nIch właściwością jest \nnie powtarzać się nigdy \nw kształtach, odcieniach, pozach i układzie. \
    \n\nNie obciążone pamięcią o niczym, \nunoszą się bez trudu nad faktami. \
    \n\nJacy tam z nich świadkowie czegokolwiek - \nnatychmiast rozwiewają się na wszystkie strony. \
    \n\nW porównaniu z chmurami \nżycie wydaje się ugruntowane, \nomalże trwałe i prawie że wieczne. \
    \n\nPrzy chmurach \nnawet kamień wygląda jak brat, \nna którym można polegać, \na one, cóż, dalekie i płoche kuzynki. \
    \n\nNiech sobie ludzie będą, jeśli chcą, \na potem po kolei każde z nich umiera, \nim, chmurom, nic do tego \nwszystkiego \nbardzo dziwnego.\
    \n\nNad całym Twoim życiem \ni moim, jeszcze nie całym, \nparadują w przepychu jak paradowały.\
    \n\nNie mają obowiązku razem z nami ginąć. \nNie muszą być widziane, żeby płynąć.\n\n(Chwila, 2002)"

###1 loop counts black characters in S

NumberOfBlackChar = 0 
for char in S:
    if char.isspace() == False :
        NumberOfBlackChar = NumberOfBlackChar + 1
print("\nNumber of black characters in the string: ", NumberOfBlackChar)

###2 number of words in S

L= S.split()                #lista słów
NumberOfElements = len(L)       #liczy elementy listy (słowa)

print("\n\nNumber of words in the string:", NumberOfElements)

####3 longest word in string
ListLenghtSorted = L
ListLenghtSorted.sort(key=len)    #sort by lenght
print("\n\nThe longest word in string: ", ListLenghtSorted[NumberOfElements-1])        #print last element of list sorted by 

print("\n\nWords sorted by lenght: ", ListLenghtSorted)

#### 4a sort by lexicographic order
ListLexicographicSorted = L
ListLexicographicSorted.sort()
print("\n\nWords in lexicographic order: ", ListLexicographicSorted)
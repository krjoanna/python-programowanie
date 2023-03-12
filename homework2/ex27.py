#dict
#Create a dict for conversion of roman numerals/strings (I, IV, V, IX, X, XL, L, XC, C, CD, D, CM, M) to arabic numbers. 
#Use different methods.

RomArabDict = {"I": 1, "V": 5, "X": 10, "L": 50}
RomArabDict["C"]= 100
RomArabDict["D"]= 500
RomArabDict["M"]= 1000

print(RomArabDict[0])
print("Write roman number: ") 
RomNumb = input()

ArabNumb = 0
i = 0
for i in range(1,7):
    ArabNumb = RomArabDict[i]
    if RomArabDict[i] > RomArabDict[i - 1]:
        ArabNumb += RomArabDict[i] - 2 * RomArabDict[i - 1]
    else:
        ArabNumb += RomArabDict[i]
    print(ArabNumb)

    j = RomArabDict[i]
    if j < ArabNumb:
        ArabNumb = ArabNumb + RomArabDict[i]

print(RomNumb, "converted to arabic numbers is: ", ArabNumb)
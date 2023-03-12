#numbers
# Find the sum 1*1 + 3*3 + 5*5 + ... + 2021*2021 [hint: use sum()].

s= sum(x*x for x in range(1,2022,2))
print("\nSum of 1*1 + 3*3 + 5*5 + ... + 2021*2021 is: "  + str(s))
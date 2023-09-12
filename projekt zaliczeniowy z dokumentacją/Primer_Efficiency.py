import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Określenie przez użytkownika ścieżki pliku w Excelu 
# Dane dla każdego startera znajdują się w osobnym arkuszu skoroszytu
#w kolumnie o tytule: "Template Dilution" --> rozcieńczenie matrycy
# w kolumnie o tytule: "Ct Value" --> wartość ct dla określonego rozcieńczenia
file_path = input(r"Enter the path to the Excel file: ")

# Otwarcie pliku w Excelu
xls = pd.ExcelFile(file_path)

# Pobranie nazw starterów z arkusza Excel
primer_names = xls.sheet_names

# Utworzenie Pandas DataFrame do przechowywania danych o efektywności starterów
efficiency_df = pd.DataFrame(columns = ["Primer Name", "Efficiency"])

# Utworzenie figury i osi na wykres z Matplotlib
fig, ax = plt.subplots()   #funkcja tworzy figure oraz osie 

n= 0.75 #punkt początkowy określający położenie legendy na figurze
# Petla przechodząca przez każdy z arkuszy (starter); wyznacza regresje, R^2, liczy wydajność starterów z regresji
for primer_name in primer_names:
    # Załadowanie danych z załadowanego arkusza Excel (xls)
    Excel_df = pd.read_excel(xls, sheet_name = primer_name)  #czyta dane z aktualnego arkusza
    
    x_values = np.log10(Excel_df['Template Dilution'].values)  #tworzy macierz zlogarytmizowanych danych z kolumny Excel_Dilution w Excel_df
    y_values = Excel_df['Ct Value'].values    #tworzy macierz z wartościami Ct

    # Wartości Ct na wykresie jako punkty
    ax.scatter(x_values, y_values, label= f'{primer_name}')

    # Zdefiniownie funkcji regresji liniowej
    def regression_function(x, a, b):
        return a * x + b

    #Dopasowanie funkcji regresji liniowej do danych x_values i y_values; uzyskanie parametrów a i b
    a_parameter, b_parameter = np.polyfit(x_values, y_values, 1)  
    
    # Wyznaczenia miary jakości dopasowania modelu R2 (1-(RSS/TSS))
    y_predicted = regression_function(x_values, a_parameter, b_parameter)
    rss = ((y_values - y_predicted)**2).sum()   #RSS (sum of squares of residuals)
    tss = ((y_values - y_values.mean())**2).sum()   #TSS (total sum of squares)
    r2 = 1 - (rss/tss)

    # Obliczenie wydajności starterów równaniem:  10^(-1/a) - 1
    efficiency = "{:.2%}".format(10 ** (-1 / a_parameter) - 1)
     # dodanie wyliczonych wartości wydajności do dataframe 
    efficiency_df = pd.concat([efficiency_df, pd.DataFrame({"Primer Name": [primer_name], "Efficiency": [efficiency]})])

    # Dodanie do wykresu krzywej dopasowania liniowego
    plt.plot(x_values, y_predicted, linestyle = "dashed")
    
    fig.text(0.85, n, f'{primer_name}'
            f'\ny = {a_parameter:.4f}x + {b_parameter:.4f}'
            f'\nR^2 = {r2:.4f} \nEfficiency={efficiency}\n\n')

    n -= 0.1  #przesunięcie tekstu w legendzie

# dopasowanie wykresu, opisanie wykresu, etc.

fig.set_size_inches(12,10)
ax.set_xlabel('log10(Template Concentration)')
ax.set_ylabel('Ct Value')
ax.set_title('Ct values for specific primers in template dilution function')
ax.legend()
ax.grid(True, color = '#a4a9ad')
plt.subplots_adjust(right=0.8)
ax.set_ylim(0)

#Pokazanie wykresu
plt.show()

# Wydrukowanie tabeli z wydajnośią starterów w terminalu
print("\nPrimer Efficiency:")
print(efficiency_df)

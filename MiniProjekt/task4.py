import pandas as pd
import matplotlib.pyplot as plt

def loadFile(fileName):
    data_frame = pd.read_csv(fileName,sep=';')
    return data_frame

def manageData(data_frame):
    data_frame['Dochód_miesięczny_PLN'] = data_frame['Dochód_miesięczny_PLN'].str.replace(',', '.')
    data_frame['Liczba_godzin_pracy_tygodniowo'] = data_frame['Liczba_godzin_pracy_tygodniowo'].str.replace(',', '.')
    data_frame['Lata_doświadczenia_zawodowego'] = data_frame['Lata_doświadczenia_zawodowego'].str.replace(',', '.')

    data_frame['Dochód_miesięczny_PLN'] = pd.to_numeric(data_frame['Dochód_miesięczny_PLN'], errors='coerce')
    data_frame['Liczba_godzin_pracy_tygodniowo'] = pd.to_numeric(data_frame['Liczba_godzin_pracy_tygodniowo'], errors='coerce')
    data_frame['Lata_doświadczenia_zawodowego'] = pd.to_numeric(data_frame['Lata_doświadczenia_zawodowego'], errors='coerce')
    bins = pd.cut(data_frame['Lata_doświadczenia_zawodowego'], bins=5)
    data_frame['Koszyk_doświadczenia'] = bins
    return data_frame 
    
def createPlot(data_frame):
    plt.figure(figsize=(10, 6))
    plt.title("Histogram Lata Doświadczenia Zawodowego")
    plt.hist(data_frame['Lata_doświadczenia_zawodowego'],bins=5,color='green', edgecolor='black')
    plt.xlabel("Lata doświadczenia")
    plt.ylabel("Częstotliwość")
    plt.savefig("task4.pdf", format="pdf")
    plt.show()
    
    
def main():
    data_frame = loadFile("hr4.csv")
    data_frame = manageData(data_frame)
    createPlot(data_frame)
    
if __name__ == "__main__":
    main()  
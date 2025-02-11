import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def loadFile(fileName):
    data_frame = pd.read_excel(fileName)
    return data_frame

def manageData(data_frame):
    trou_data = data_frame.iloc[0:0].copy()
    hake_data = data_frame.iloc[0:0].copy()
    herr_data = data_frame.iloc[0:0].copy()
    trou_data = data_frame[data_frame["Rodzaje produktów"] == "pstrąg świeży niepatroszony - za 1 kg"].copy()
    hake_data = data_frame[data_frame["Rodzaje produktów"] == "filety z morszczuka mrożone - za 1kg"].copy()
    herr_data = data_frame[data_frame["Rodzaje produktów"] == "śledź solony, niepatroszony - za 1kg"].copy()
    return trou_data,hake_data,herr_data 

def createPlot(trou_data,hake_data,herr_data):
    x = np.arange(7) 
    plt.figure(figsize=(10, 6))
    plt.title("Ceny za 1kg ryb w kolejnych latach")
    plt.scatter(x,trou_data['Wartosc'],color='r',  marker='o', s=125)
    plt.scatter(x,hake_data['Wartosc'],color='b', marker='^', s=175)
    plt.scatter(x,herr_data['Wartosc'],color='g', marker='s', s=75)
    plt.xticks(x,trou_data['Rok'])
    plt.legend(["Pstrąg","Morszczuk","Śledź"], loc="center right")
    plt.xlabel("Lata")
    plt.ylabel("Cena[zł]")
    plt.grid(True)
    plt.savefig("task6.webp", format="webp")
    plt.show()
    
def main():
    data_frame = loadFile("ceny5.xlsx")
    trou_data,hake_data,herr_data  = manageData(data_frame)
    createPlot(trou_data,hake_data,herr_data)

if __name__ == "__main__":
    main()
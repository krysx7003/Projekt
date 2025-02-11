import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def loadFile(fileName):
    data_frame = pd.read_csv(fileName)
    print(data_frame)
    return data_frame

def manageData(data_frame):
    column = data_frame.columns[0]
    columns = column.split(' ')
    new_data = pd.DataFrame(columns=columns)
    for x in data_frame.index:
        value = data_frame.loc[x,'Marka 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019']
        values = value.split(' ')
        if x==2:
            values[0] = values[0]+' '+values[1]
            del values[1]
        new_data.loc[x] = values
    new_data = new_data.melt(id_vars=['Marka'], var_name='Rok', value_name='Liczba_Pasażerów')
    new_data['Rok'] = new_data['Rok'].astype(int)
    new_data['Liczba_Pasażerów'] = pd.to_numeric(new_data['Liczba_Pasażerów'], errors='coerce')
    eur_data = new_data.iloc[0:0].copy()
    amt_data = new_data.iloc[0:0].copy()
    eur_data = new_data[new_data["Marka"] == "Eurostar"].copy()
    amt_data = new_data[new_data["Marka"] == "Amtrak"].copy()
    return eur_data,amt_data 

def createPlot(eur_data,amt_data):
    x = np.arange(10) 
    width = 0.2
    plt.figure(figsize=(10, 6))
    plt.subplots_adjust( hspace=0.4)
    plt.subplot(2, 1, 1)
    plt.title("Liczba pasażerów w kolejnych latach dla Eurostar")
    plt.bar(x,eur_data['Liczba_Pasażerów'],width, color='orange')
    plt.xticks(x,eur_data['Rok'])
    plt.legend(["Eurostar"], loc="center right")
    plt.xlabel("Lata")
    plt.ylabel("Liczba pasażerów")
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.title("Liczba pasażerów w kolejnych latach dla Amtrak")
    plt.bar(x,amt_data['Liczba_Pasażerów'],width, color='green' )
    plt.xticks(x,amt_data['Rok'])
    plt.legend(["Amtrak"], loc="center right")
    plt.xlabel("Lata")
    plt.ylabel("Liczba pasażerów")
    plt.grid(True)

    plt.savefig("task3.eps", format="eps")
    plt.show()
    
def main():
    data_frame = loadFile("koleje3.csv")
    eur_data,amt_data  = manageData(data_frame)
    createPlot(eur_data,amt_data)

if __name__ == "__main__":
    main()
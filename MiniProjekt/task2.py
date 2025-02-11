import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def loadFile(fileName):
    data_frame = pd.read_excel(fileName)
    return data_frame

def manageData(data_frame):
    lubel_data = data_frame.iloc[0:0].copy()
    lubus_data = data_frame.iloc[0:0].copy()
    lubel_data = data_frame[data_frame["Nazwa"] == "LUBELSKIE"].copy()
    lubus_data = data_frame[data_frame["Nazwa"] == "LUBUSKIE"].copy()
    print(lubel_data)
    print(lubus_data)
    return lubel_data,lubus_data

def createPlot(lubel_data, lubus_data):
    x = np.arange(4) 
    width = 0.2
    plt.figure(figsize=(10, 6))
    plt.title("Języki nauczane w wybranych województwach")
    plt.bar(x-width,lubel_data['Wartość'],width, color='orange')
    plt.bar(x,lubus_data['Wartość'],width, color='green' )
    plt.xticks(x,lubel_data['Języki obce'])
    plt.legend(["Woj. Lubelskie", "Woj. Lubuskie"], loc="center right")
    plt.xlabel("Języki")
    plt.ylabel("Liczba uczniów [osoby]")
    plt.grid(True)
    plt.savefig("task2.jpg", format="jpg")
    plt.show()
    
def main():
    data_frame = loadFile("jezykiobce2.xlsx")
    lubel_data, lubus_data = manageData(data_frame)
    createPlot(lubel_data, lubus_data)
    
if __name__ == "__main__":
    main()
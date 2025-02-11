import pandas as pd
import matplotlib.pyplot as plt

def loadFile(fileName):
    data_frame = pd.read_excel(fileName)
    return data_frame

def manageData(data_frame):
    for x in data_frame.index:
        if data_frame.loc[x, "Wartość"] < 80:
            data_frame.drop(x, inplace = True)
    return data_frame 

def createPlot(data_frame):
    colors = ['pink', 'silver', 'steelblue','green', 'blue']
    plt.figure(figsize=(10, 6))
    plt.title("Zestawienie danych 1")
    plt.pie(data_frame['Wartość'],labels=data_frame['Nazwa'],colors=colors, autopct='%1.1f%%')
    plt.savefig("task1.pdf", format="pdf")
    plt.show()
    
def main():
    data_frame = loadFile("licea1.xlsx")
    data_frame = manageData(data_frame)
    createPlot(data_frame)
    
if __name__ == "__main__":
    main()
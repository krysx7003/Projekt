import pandas as pd
import math

columnList = ['Colum1','Colum2','Colum3','Colum4','Colum5']
data_frame = pd.DataFrame()
test_frame = pd.DataFrame()
valid_frame = pd.DataFrame()
train_frame = pd.DataFrame()
def loadData(fileName,firstRowIsHeader):
    global data_frame,columnList
    with open(fileName, 'r') as file:
        i=0
        if firstRowIsHeader:
            i +=1
            line = file.readline() 
            columnList = line.strip().split(',')
        data_frame = pd.DataFrame(columns=columnList)
       
        for line in file:
            values = line.strip().split(',')
            if len(values)==5:
                data_frame.loc[i] = values
            i += 1

def printHeaders():
    if columnList[0] != 'Colum1':
        print(data_frame)
    else:
        print("Nie wczytano nagłówków")

def printData(start = 0,stop = None):
    if stop is None:
        stop = len(data_frame) 
    print(data_frame.loc[start:stop])

def splitData(train,test,valid):
    global train_frame,test_frame,valid_frame
    size = len(data_frame)
    train = math.floor(train*size)
    test = math.floor(test*size)
    valid =  math.floor(valid*size)
    train_frame = data_frame.loc[:train]
    print(str(len(train_frame)))
    train +=1
    test_frame = data_frame.loc[train:train+test]
    print(str(len(test_frame)))
    valid_frame = data_frame.loc[train+test+1:]
    print(str(len(valid_frame)))

def countClasses():
    decision_counts = data_frame[columnList[4]].value_counts()
    decision_tuples = list(decision_counts.items())
    print(f"Liczba klas decyzyjnych: {len(decision_counts)}")
    print("Klas decyzyjnych i liczba wystąpień:")
    print(decision_tuples)

def printClass(clasName):
    i = 0
    class_frame = data_frame.iloc[0:0].copy()
    for x in data_frame.index:
        value = data_frame.loc[x]
        if value.loc[columnList[4]] == clasName:
            class_frame.loc[i] = value
            i += 1
    print(class_frame)

def saveData(dataList,fileName):
    dataList.to_csv(fileName,header=False, index=False)

import pandas as pd
import seaborn as snb
import matplotlib.pyplot as plt
import numpy as nf
import csv

data = pd.read_csv("/Users/tahayasinmucak/Desktop/Yazilim1/Deneme/Python/MasterStudy/modified_dataset.csv")
# data.replace(",", ".", regex=True, inplace=True)
# data[["08Sep2022", "18Sep2022", "28Sep2022", "08Oct2022"]] = data[["08Sep2022", "18Sep2022", "28Sep2022", "08Oct2022"]].astype(float)
data.set_index("Pot", inplace=True)  # Index düzeltme

# data.to_csv("/Users/tahayasinmucak/Desktop/Yazilim1/Deneme/Python/MasterStudy/modified_dataset.csv")


##To get the reflesh data
def dataRead():
    newData =pd.read_csv("/Users/tahayasinmucak/Desktop/Yazilim1/Deneme/Python/MasterStudy/modified_dataset.csv")
    return newData


chard =dataRead()[dataRead()['Crop']=="Chard"] ## We creat a dataset for chard
clover =dataRead()[dataRead()['Crop']=="Clover"] ## We creat a dataset for Clover


###To see the all the value of selected crop
def dataset(user):
    info =dataRead()[dataRead()['Crop']==user] 
    return info
def datasetAn(user):
    info =dataRead()[dataRead()['Crop']==user][['08Sep2022','18Sep2022','28Sep2022','08Oct2022']].describe().round()
    return info


###Replace Function
# def replace(pot,date,value):
#     data.loc[pot, date] = value
#     return data
#Add Data

def add(pot, treatment, crop, date, value):
    add_data = [pot, treatment, crop, date, value]
    valid_pot_no = list(range(len(dataRead()) + 1))
    
    if pot in valid_pot_no:
        print("This pot number already exists.")
        return data
    
    with open("/Users/tahayasinmucak/Desktop/Yazilim1/Deneme/Python/MasterStudy/modified_dataset.csv", 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(add_data)
    return  dataRead()

##Replace
def replace(pot,date,value):
    data=dataRead()
    validpotno = list(range(len(data)+1))
    if pot in validpotno:
        data.loc[pot, date] = value
        data.to_csv("/Users/tahayasinmucak/Desktop/Yazilim1/Deneme/Python/MasterStudy/modified_dataset.csv", index=False)
        return dataRead()
    else:
        print("No way man")

 ## Delete Data from database 
def delete(pot,date):
    data = dataRead()
    validpot = list(range(len(data)+1))
    if pot in validpot:
        data.loc[pot,date]=None
        data.to_csv("/Users/tahayasinmucak/Desktop/Yazilim1/Deneme/Python/MasterStudy/modified_dataset.csv", index=False)
        return  dataRead()
    else:
        print("The Pot number that you enter is not valid")


##Nulldata
def null(value):
    info =dataRead()[dataRead()['Crop']==value].isnull().sum()
    return info

def Mono(crop):
    data=dataRead()
    newdata = data[(data['Crop'] == crop) & (data['Treatment'] == 'Mono')]
    return newdata
def Pre(crop):
    newdata = data[(data['Crop'] == crop) & (data['Treatment'] == 'Pre')]
    return newdata
def Same(crop):
    newdata = data[(data['Crop'] == crop) & (data['Treatment'] == 'Same')]
    return newdata


##Grafik
def display():

    selected_data = dataRead().loc[dataRead()['Treatment'].isin(["Same", "Pre", "Mono"]), :]
    crops = dataRead()["Crop"].unique()

    fig, ax = plt.subplots(figsize=(10, 6))
    snb.barplot(x="Crop", y="08Oct2022", hue="Treatment", data=selected_data, ci="sd", ax=ax, errcolor="black", errwidth=2.5, capsize=0.01)
    ax.set_xlabel("Treatment")
    ax.set_ylabel("Mean Root Growth (cm)")
    ax.set_title("Root Growth by Crop and Treatment 08.10.2022")
    ax.legend()
    return plt.show()
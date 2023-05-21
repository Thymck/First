import pandas as pd
import seaborn as snb
import matplotlib.pyplot as plt
import numpy as nf


data = pd.read_csv("/Users/tahayasinmucak/Desktop/Yazilim1/Deneme/Python/MasterStudy/Resultsofroots.csv")
data = data.replace(",", ".", regex=True)
data[["08Sep2022", "18Sep2022", "28Sep2022", "08Oct2022"]] = data[["08Sep2022", "18Sep2022", "28Sep2022", "08Oct2022"]].astype(float)

data=data.set_index("Pot") ## Index düzeltme

chard =data[data['Crop']=="Chard"] ## We creat a dataset for chard
clover =data[data['Crop']=="Clover"] ## We creat a dataset for Clover

def dataset(user):
    info =data[data['Crop']==user] 
    return info
def datasetAn(user):
    info =data[data['Crop']==user].describe().round() 
    return info

###Replace Function
# def replace(pot,date,value):
#     data.loc[pot, date] = value
#     return data
#deneme

def deneme():
    pass


def replace(pot,date,value):
    validpotno = list(range(len(data)+1))
    if pot in validpotno:
        data.loc[pot, date] = value
        return data
    else:
        print("No way man")

 ## Delete Data from database 
def delete(pot,date):
    validpot = list(range(len(data)+1))
    if pot in validpot:
        data.loc[pot,date]=None
        return data
    else:
        print("Oww boy the pot no not exist")


##Nulldata
def null(value):
    info =data[data['Crop']==value].isnull().sum()
    return info


##Grafik
def display():

    selected_data = data.loc[data['Treatment'].isin(["Same", "Pre", "Mono"]), :]
    crops = data["Crop"].unique()

    fig, ax = plt.subplots(figsize=(10, 6))
    snb.barplot(x="Crop", y="08Oct2022", hue="Treatment", data=selected_data, ci="sd", ax=ax, errcolor="black", errwidth=2.5, capsize=0.01)
    ax.set_xlabel("Treatment")
    ax.set_ylabel("Mean Root Growth (cm)")
    ax.set_title("Root Growth by Crop and Treatment 08.10.2022")
    ax.legend()
    return plt.show()
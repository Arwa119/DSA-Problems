import matplotlib.pyplot as plt
import pandas as pd 

def Smptom_Dis():
    df = pd.read_csv('Train.csv')           # Load the data
    diesease = df.columns[:-1]
    label = df['TYPE']
    for i in diesease:
        plt.figure(figsize=(6, 4))          #plotting graphs between each disease and symptoms
        plt.scatter(df[i], label)
        plt.title(f"Scatter plot of {i} vs Disease Label")
        plt.xlabel(i)
        plt.ylabel('Disease Label')
        plt.show()

if __name__ == "__main__":
    Smptom_Dis()
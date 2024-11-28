import matplotlib.pyplot as plt
import pandas as pd 

#1
def daily_steps():
    df = pd.read_csv('dailySteps_merged.csv')
    df['ActivityDay'] = pd.to_datetime(df['ActivityDay'])
    grouped_df = df.groupby('ActivityDay')['StepTotal'].sum().reset_index()
    list1 = grouped_df['ActivityDay'].values
    list2 = grouped_df['StepTotal'].values
    plt.title('Daily Steps')
    plt.xlabel("ActivityDay")
    plt.ylabel("StepTotal")
    plt.plot(list1, list2)
    plt.show()

# 2
def daily_distance():    
    df = pd.read_csv('dailyActivity_merged.csv')
    df['ActivityDate'] = pd.to_datetime(df['ActivityDate'])
    grouped_df = df.groupby('ActivityDate')['TotalDistance'].sum().reset_index()
    grouped_df=grouped_df.sort_values('ActivityDate')
    list1 = grouped_df['ActivityDate'].values
    list2 = grouped_df['TotalDistance'].values
    plt.bar(list1, list2)
    plt.title('Daily distance')
    plt.xlabel("ActivityDate")
    plt.ylabel("TotalDistance")
    plt.show()

# #3
def Total_sleep():
    df = pd.read_csv('sleepDay_merged.csv')
    df['SleepDay'] = pd.to_datetime(df['SleepDay'])
    grouped_df = df.groupby('SleepDay')['TotalMinutesAsleep'].sum().reset_index()
    grouped_df = grouped_df.sort_values('SleepDay')
    list1 = grouped_df['SleepDay'].values
    list2 = grouped_df['TotalMinutesAsleep'].values
    plt.scatter(list1, list2)
    plt.title('Daily Sleep')
    plt.xlabel("SleepDay")
    plt.ylabel("TotalMinutesAsleep")
    plt.show()

#4
def hourly_steps():
    df = pd.read_csv('hourlySteps_merged.csv')
    df['ActivityHour'] = pd.to_datetime(df['ActivityHour'])
    filtered_df = df[df['ActivityHour'].dt.date == pd.to_datetime('2016-04-12').date()]
    list1 = filtered_df['ActivityHour'].dt.strftime('%H:%M').values
    list2 = filtered_df['StepTotal'].values
    list1 = list1[:15]
    list2 = list2[:15]  
    plt.pie(list2, labels=list1, autopct='%1.1f%%')
    plt.title('Hourly Steps on 12th April 2016')
    plt.show()

if __name__ == "__main__":
    daily_steps()
    daily_distance()
    Total_sleep()
    hourly_steps()
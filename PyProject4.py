import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv("data export.csv")
#print(df.head())

df.columns = df.iloc[0]
df=df.drop(index=0).reset_index(drop=True)
#print(df.head())

df.columns=["channel group","Datehour","Users","Sessions","Engaged sessions","Average engagement time per session","Engaged sessions per user","Events per session","Engagement rate","Event count"]
#print(df.info())

df["Datehour"]=pd.to_datetime(df["Datehour"],format="%Y%m%d%H",errors="coerce")
numeric_cols= df.columns.drop(["channel group","Datehour"])
df[numeric_cols]=df[numeric_cols].apply(pd.to_numeric,errors="coerce")
df["Hour"]=df["Datehour"].dt.hour
#print(df.head())
#print(df.describe())
#print(df.isnull().sum())
'''
sns.set(style="whitegrid")
plt.figure(figsize=(10,5))
df.groupby("Datehour")[["Sessions","Users"]].sum().plot(ax=plt.gca())
plt.title("Sessions and users over time")
plt.xlabel("DateHour")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(data= df,x="channel group",y="Users",estimator=np.sum,palette="viridis")
plt.title("Total users by channel")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(data= df,x="channel group",y="Average engagement time per session",estimator=np.mean,palette="magma")
plt.title("Avg engagement time by channel")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(data= df,x="channel group",y="Engagement rate",palette="coolwarm")
plt.title("Engagement rate distribution by channel")
plt.xticks(rotation=45)
plt.show()
'''
df_plot = df.groupby("Datehour")[["Engagement rate","Sessions"]].mean().reset_index()
plt.figure(figsize=(10,5))
plt.plot(df_plot["Datehour"],df_plot["Engagement rate"],label="Engagement rate",color="green")
plt.plot(df_plot["Datehour"],df_plot["Sessions"],label="Sessions",color="blue")
plt.title("Engagement rate vs Sessions over time")
plt.xlabel("DateHour")
plt.legend()
plt.grid(True)
plt.show() 
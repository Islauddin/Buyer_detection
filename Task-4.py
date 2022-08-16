import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("orders_2016-2020_Dataset.csv")

#The shipping address differs from the billing address
def diff_shipp_diff_bill():
    address=df[df["Billing Street Address"]!=df['Shipping Street Address']]['Shipping Street Address']
    data_frame=pd.DataFrame({'Shipping Street Address':address}).value_counts()
    Data_frame=pd.DataFrame({'No of times shipping':data_frame})
    c=input("Enter Excel file name :")
    csv_file=Data_frame.to_csv(c)
    df1=pd.read_csv(c)
    h=df1["Shipping Street Address"].value_counts()[:30].plot(kind='barh',figsize=(20,10))
    plt.gca().invert_yaxis()
    plt.show()
    return csv_file


#Multiple orders of the same item
def Mul_order_same_item():
    item=df['LineItem Name']
    order=pd.DataFrame({'Item Name':item}).value_counts()
    Data_frame=pd.DataFrame({"No of times of Orders":order})
    d=input('Enter Excel File Name:')
    csv_file=Data_frame.to_csv(d)

    h=df['LineItem Name'].value_counts().head(30)
    fig , ax = plt.subplots(figsize=(100,70))
    h.plot(kind='barh')
    ax.tick_params(axis='y', labelsize= 15)
    ax.tick_params(axis='x', labelsize= 15)
    plt.gca().invert_yaxis()
    plt.show()
    return csv_file

#Unusually large orders
def Unusually_large_order():
    Data=[]
    df["new_data"]=df["LineItem Sale Price"].str.split("₹").apply(lambda x:x[1])
    for i in df["new_data"]:
        S=i.replace(",",'')
        value=float(S)
        Data.append(value)
    Data_frame=pd.DataFrame(Data)
    df['new_data1']=Data_frame
    order=df[df["new_data1"]>20000]['LineItem Name']
    price=df[df["new_data1"]>20000]["Total"]
    data_frame1=pd.DataFrame({"LineItem Name":order,"Total":price}).value_counts()
    Data_frame=pd.DataFrame({"Number Of Item":data_frame1})
    b=input("Enter Excel file Name :")
    csv_file=Data_frame.to_csv(b)
    df3=pd.read_csv(b)
    df3['Total'].value_counts().plot(kind='bar')
    plt.show()
    return csv_file

#Multiple orders to the same address with different payment method
def diff_pay_mul_order_same_add():
    diffrent=pd.DataFrame({'No of multiple orders':df.groupby(['Payment Method',"Shipping Street Address",'LineItem Name'])['LineItem Name'].count()})
    e=input("Enter your excel file name:")
    csv_file=diffrent.to_csv(e)
    df4=pd.read_csv(e)
    df4['Payment Method'].dropna().str.split().apply(lambda x:x[0]).value_counts().plot(kind='pie',autopct='%0.2f%%',figsize=(20,10))
    plt.show()
    return csv_file

#Unexpected international orders
def International_orders():
    Name=df[df["Shipping Country"]!='IND']['LineItem Name']
    price=df[df["Shipping Country"]!='IND']['Total']
    status=df[df["Shipping Country"]!='IND']["Payment Status"]
    country=df[df['Shipping Country']!='IND']['Shipping Country']
    international_orders=pd.DataFrame({'LineItem Name':Name,'Price':price,'order status':status,'Shipping Country':country})
    a=input("Enter Your csv file Name :")
    csv_file=international_orders.to_csv(a)
    df5=pd.read_csv(a)
    df5['Shipping Country'].value_counts().plot(kind='bar')
    plt.show()
    return csv_file

str="""Enetr 1 for The shipping address differs from the billing address
    Enter 2 for Multiple orders of the same item
    Enetr 3 for Unusually large orders
    Enter 4 Multiple orders to the same address with different payment method
    Enter 5 Unexpected international orders"""

while True:
    print(str)
    num=int(input("Enter your choice:"))
    if num==1:
        diff_shipp_diff_bill()
    elif num==2:
        Mul_order_same_item()
    elif num==3:
        Unusually_large_order()
    elif num==4:
        diff_pay_mul_order_same_add()
    elif num==5:
        International_orders()
    elif num==6:
        break


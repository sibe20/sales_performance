import pandas as pd  
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('ggplot')
pd.set_option('display.max_column', None)
df =pd.read_csv(r'C:/Users/SPECIAL TEK/Downloads/sales/sales_data_sample.csv', encoding='latin1')
no_of_na=df.isna().sum()#counting the number of na 
del df["ADDRESSLINE2"] #delete single column
no_of_na=df.isna().sum()
df=df.drop(["TERRITORY","STATE"], axis=1)#delete multiple columns 
no_of_na=df.isna().sum()#all big number columns of na has deleted 
df=df.fillna(0)
'''print(df["POSTALCODE"].isna().sum())
print(df.isna().sum())'''

#data type
#==========
#print(df.columns)
'''print(df[['ORDERNUMBER','QUANTITYORDERED','PRICEEACH','ORDERLINENUMBER','SALES', 'ORDERDATE', 'STATUS', 'QTR_ID', 'MONTH_ID', 'YEAR_ID',
       'PRODUCTLINE', 'MSRP', 'PRODUCTCODE', 'CUSTOMERNAME', 'PHONE',
       'ADDRESSLINE1', 'CITY', 'POSTALCODE', 'COUNTRY', 'CONTACTLASTNAME',
       'CONTACTFIRSTNAME', 'DEALSIZE']].dtypes)'''

#these columns types are incorrect
#_________________________________________________________________________________________________________
#ORDERDATE, STATUS,PRODUCTLINE,MSRP,PRODUCTCODE,CUSTOMERNAME,PHONE,ADDRESSLINE1,CITY,POSTALCODE,COUNTRY,CONTACTLASTNAME
#CONTACTFIRSTNAME DEALSIZE
#________________________________________________________________________________________________________
df['ORDERDATE']=pd.to_datetime(df['ORDERDATE'])
df[['STATUS','PRODUCTLINE','CITY','COUNTRY','DEALSIZE']]=df[['STATUS','PRODUCTLINE','CITY','COUNTRY','DEALSIZE']].astype("category")
df['MSRP']=df['MSRP'].astype(float)
df[['PRODUCTCODE','CUSTOMERNAME','PHONE','ADDRESSLINE1','POSTALCODE','CONTACTLASTNAME','CONTACTFIRSTNAME']]=df[['PRODUCTCODE','CUSTOMERNAME','PHONE','ADDRESSLINE1','POSTALCODE','CONTACTLASTNAME','CONTACTFIRSTNAME']].astype(pd.StringDtype())
#print("typeee")
#print(df[['STATUS','PRODUCTLINE','MSRP','PRODUCTCODE','CUSTOMERNAME','PHONE','ADDRESSLINE1','CITY','POSTALCODE','COUNTRY','CONTACTLASTNAME','CONTACTFIRSTNAME']].dtypes)


#check for duplicates 
#=====================
duplicates =df.duplicated()
or_duplicate=df.duplicated(subset='ORDERNUMBER')
#print(df.loc[or_duplicate])
#print("sum of duplicate",duplicates.sum())


#check  that have the same one column what other diffrences have 
x=df.query('ORDERNUMBER==10107')
#print(x)

#mean and meadian etc....
#print(df.describe())

#change the column name 
new_column_name=df.rename(columns={'ADDRESSLINE1':'ADDRESS', 'MSRP': 'COST_PRICE'})
#print(new_column_name.columns)



#show two feature relation
value_counts=df[df['COUNTRY']=='USA']['CITY'].value_counts()
value_counts=value_counts[value_counts>0]
graphed=value_counts.plot(kind='bar', title="the number of customer in each city in US") 
#other types of bars -> hist ,kde(plot)
graphed.set_xlabel('city ')
graphed.set_ylabel('number of customers ')
#print(value_counts)
#plt.show()



#combine the orders that have the same order number as x
x=df.groupby('ORDERNUMBER').agg({
    
   'QUANTITYORDERED' : 'sum',
   'PRICEEACH': 'sum', 
   'COUNTRY': 'first'
   
})

#print(x)

#show five features relation in graph
#sns.pairplot(df,vars=['QUANTITYORDERED', 'YEAR_ID' ,'PRICEEACH','SALES'],hue='STATUS')
#plt.show()


#heatmap to show the correlation 
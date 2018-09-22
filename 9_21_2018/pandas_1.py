#pandas
import pandas as pd
#excel - read_excel
data  = pd.read_csv("pandas_csv.csv")
#print data

#head and tail..
print data.head()
print "="*30
print data.tail()
print data.shape

#rows and columns..iloc..
print data.iloc[1:3] #[start row : end row]
print data.iloc[-2:]

#loc..
print data.loc[:2]

#rows by columns
print data[data["score"] > 50]

print data.loc[:3,["score","title"]]
print "="*10
#multiple filers..
print data[ (data["score"] > 50) & (data["length"] > 5)]

print data[["title"]]

#methods:
print data["score"].mean()
print data["score"]/2
print data["score"] > 90

data["club"] = data["score"] + data ["length"]
print data["club"]


print data.isin([2,4])

print data.sort_values("score",ascending=True)

print data["score"].count()
print data["score"].max()

print "="*30
print data

data.to_csv("datawrite.csv",index=False)

















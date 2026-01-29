import pandas as pd

df=pd.read_csv("data.csv")

print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.min(numeric_only=True))
print(df.max(numeric_only=True))
group= df.groupby("Type 1")

print(group)
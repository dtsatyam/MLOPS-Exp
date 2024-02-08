import pandas as pd

Data = [
    {"name":'satya', "age":38, "city":"Bangalore"},
    {"name":'Sandhya', "age":34, "city":"Podili"},
    {"name":'Bhuvan', "age":10, "city":"Chimakurthy"},
    {"name":'Mokshith', "age":6, "city":"Chimakurthy"}
]
Data = pd.DataFrame(Data)

Data.to_csv("data/data.csv", index=False)
import pandas as pd

path = r"C:\Users\ramda\OneDrive\Desktop\data"

with open(path, "r") as file:
    content = file.read()
    print(content)
df = pd.read_csv(path)
print(df)

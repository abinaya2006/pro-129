import pandas as pd

df = pd.read_csv("dwarf_stars.csv")

df["Radius"] = 0.102763*df["Radius"]
df["Mass"] = 0.000954588*df["Mass"]
df.dropna()
df.to_csv("unit_converted_stars.csv")
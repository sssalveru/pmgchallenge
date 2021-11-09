import sys
import pandas as pd

first_arg = sys.argv[1]

list = []
for i in sys.argv[1:]:
    df = pd.read_csv(f"{i}")
    df['filename'] = i
    list.append(df)

frame = pd.concat(list)
frame.to_csv("output.csv")
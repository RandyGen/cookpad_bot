import pandas as pd
import glob

# path = r'C:\DRO\DCL_rawdata_files'
all_files = glob.glob("recipe_data/*.csv")

li = []
# print(all_files)

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)
    # print(li)

frame = pd.concat(li, axis=0, ignore_index=True)
print(frame.head())

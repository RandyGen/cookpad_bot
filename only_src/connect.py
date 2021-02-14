import glob
import pandas as pd

DATA_PATH = "recipe_data/"
All_Files = glob.glob('{}*.csv'.format(DATA_PATH))

list = []
for file in All_Files:
    list.append(pd.read_csv(file))

df = pd.concat(list, sort=False)

df.to_csv('all_recipes.csv', index=False)

print("Connect Perfect")

# この後にcsvをtxtへ

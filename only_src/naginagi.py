import nagisa
import pandas as pd
import pathlib

text_file = open("all_recipes.txt", "r", encoding='UTF-8', errors='ignore')
texts = text_file.readlines()
parsed_text = ''

print("Text Ready...")

# Parse text using nagisa
for text in texts:
   if str(nagisa.wakati(text) == "。"):
      parsed_text += "\n"
   parsed_text += ' '.join(nagisa.wakati(text))

print('Parsing ok')

# df = pd.DataFrame({'parsed_text': parsed_text})
# fpath = pathlib.Path("Twitterbot") / "parsed_data.csv"
# parsed_text.to_csv(fpath, index=False)
file = open('parsed_data.txt', 'w', encoding='UTF-8', errors='ignore')
file.write(parsed_text)
file.close()
print("File done")
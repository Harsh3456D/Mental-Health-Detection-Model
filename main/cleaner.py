import pandas as pd
import numpy as np
import html
import re


data = pd.read_csv('app\main\dataset\\val.csv')
df = pd.DataFrame(data)

df.replace(r'^\s*$', np.nan, regex=True,inplace=True)
# df['index'] = pd.to_numeric(df['index'] , errors='coerce')
df.dropna(subset=['statement','status'], how='any')

def clean_text(text):
    if not isinstance(text, str):
        return ""

    text = html.unescape(text)
    
    text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    
    text = re.sub(r'http\S+|www\.\S+', '', text)
    
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

# index = {}

# if df['status']!= index:
#     index = 

prefixToRemove = 'self.'

df['statement'] = df['statement'].apply(clean_text)
df.replace(r'^\s*$', np.nan, regex=True, inplace=True)
df['status'] = df['status'].str.replace(prefixToRemove, '', regex=False)
df.dropna(subset=['statement'], inplace=True)
# df['index'] = df['index'].astype(int)
df.to_csv('app\main\dataset\cleanDataVal.csv', index=True)


print(f"Done! Saved {len(df)} rows to: app\main\dataset")
print(f"Cleaned {len(data) - len(df)} rows")

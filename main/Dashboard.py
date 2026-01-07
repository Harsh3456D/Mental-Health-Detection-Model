import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


fig = plt.figure(figsize=(16, 10))
fig.suptitle('Mental Health Data Dashboard', fontsize=20, fontweight='bold')

data = pd.read_csv('app\\main\\dataset\\cleanData.csv')
df = pd.DataFrame(data)
plt.style.use('ggplot')



xbar = np.array(df['index'])
ybar = np.array(df['status'])
plt.subplot(2,2,1)
plt.bar(ybar,xbar)
plt.xlabel('Number of Entries')
plt.ylabel('Types of Problems')


ypie = df['status'].value_counts()
plt.subplot(2,2,2)
plt.pie(ypie, labels=ypie.index, autopct='%1.1f%%')



df['length'] = df['statement'].astype(str).apply(len)
avgLengthStatus = df.groupby('status')['length'].mean()
plt.subplot(2,2,3)
plt.bar(avgLengthStatus.index, avgLengthStatus.values, color='purple')
plt.xlabel("Avg Character count in text")

plt.subplot(2,2,4)
plt.hist(df['length'], bins=50)
plt.title('Distributiion of statement length')
plt.xlabel('Length of text')
plt.ylabel('Frequency')


plt.tight_layout()
plt.show()

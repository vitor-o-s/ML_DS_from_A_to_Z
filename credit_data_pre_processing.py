import pandas as pd
import numpy as np

df = pd.read_csv('credit-data.csv')
df.describe()

df.loc[df['age'] < 0]

#df.drop('age', 1, inplace=True)
#df.drop(base[base.age < 0].index, inplace=True)

#df.mean()
#df['age'].mean()
df['age'][df.age > 0].mean()
df.loc[df.age < 0, 'age'] = 40.92

pd.isnull(base['age'])
base.loc[pd.isnull(base['age'])]

previsores = base.iloc[:, 1:4].values
classe = base.iloc[:, 4].values

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(previsores[:, 0:3])
previsores[:, 0:3] = imputer.transform(previsores[:,0:3])

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

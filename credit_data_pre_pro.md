## Credit Data pre processing explained

We start importing some libraries to work with data
```python 
import pandas as pd
import numpy as np
```
Now we can import or database
```python 
df = pd.read_csv('credit-data.csv')
```
If  you want see the table 
```python
df.describe()
```
# Inconsistent Data
So we will looking for inconsistent data, in this case where age < 0
```python
df.loc[df['age'] < 0]
```
To fix this we have 3 means:

1. Drop column 
```python
df.drop('age', 1, inplace=True)
```
2. Drop only the registers
```python
df.drop(base[base.age < 0].index, inplace=True)
```
3. Or the best way, search for missing values ​​and replace them
```python
df.mean()
df['age'].mean()
#If you use the age column without selecting you will get a false average
df['age'][df.age > 0].mean()
df.loc[df.age < 0, 'age'] = 40.92
```
# Here we will treat missing data

See if we have nan data
```python
pd.isnull(base['age'])
base.loc[pd.isnull(base['age'])]
```
We separate the classes
```python
previsores = base.iloc[:, 1:4].values
classe = base.iloc[:, 4].values
```
We can then perform the correction of the missing data
```python
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(previsores[:, 0:3])
previsores[:, 0:3] = imputer.transform(previsores[:,0:3])
```
# Changing scales
Sometimes it is necessary to change scales, since the difference can interfere with the performance of the algorithms
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)
```

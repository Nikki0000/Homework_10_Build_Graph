import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
one_hot_encoded = pd.get_dummies(data['whoAmI'], prefix='whoAmI')
data_encoded = pd.concat([data.drop(columns=['whoAmI']), one_hot_encoded], axis=1)
data_encoded.head()
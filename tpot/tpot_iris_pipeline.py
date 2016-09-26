import numpy as np
import pandas as pd

from sklearn.cross_validation import train_test_split
from sklearn.svm import LinearSVC

# NOTE: Make sure that the class is labeled 'class' in the data file
tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR')
training_indices, testing_indices = train_test_split(tpot_data.index, stratify = tpot_data['class'].values, train_size=0.75, test_size=0.25)

result1 = tpot_data.copy()

# Perform classification with a LinearSVC classifier
lsvc1 = LinearSVC(C=50.0, penalty="l1", dual=False, random_state=42)
lsvc1.fit(result1.loc[training_indices].drop('class', axis=1).values, result1.loc[training_indices, 'class'].values)

result1['lsvc1-classification'] = lsvc1.predict(result1.drop('class', axis=1).values)

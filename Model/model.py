from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import joblib

dataset = pd.read_csv("glass.csv")

X = dataset.iloc[:, :-1]
y = dataset.iloc[:, 9]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42)

sc_x = StandardScaler()
X_train = sc_x.fit_transform(X_train)
X_test = sc_x.transform(X_test)

cls = RandomForestClassifier(
    criterion='entropy', n_estimators=300, random_state=42)
cls.fit(X_train, y_train)

print('ACCURACY is ', cls.score(X_test, y_test)*100, '%')

# save
filename = 'finalized_model.sav'
joblib.dump(cls, filename)

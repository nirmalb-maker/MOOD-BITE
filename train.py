import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import pickle

data = pd.read_csv("data.csv")

encoders = {}

for column in ["taste", "budget", "meal_type", "company", "diet"]:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    encoders[column] = le

X = data[["taste", "budget", "meal_type", "company", "diet"]]
y = data["dish"]

model = DecisionTreeClassifier()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(encoders, open("encoders.pkl", "wb"))

print("✅ Model trained and saved!")

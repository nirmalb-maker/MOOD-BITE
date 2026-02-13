from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load model + encoders
model = pickle.load(open("model.pkl", "rb"))
encoders = pickle.load(open("encoders.pkl", "rb"))
data = pd.read_csv("data.csv")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/recommend', methods=["POST"])
def recommend():

    taste = request.form["taste"]
    budget = request.form["budget"]
    meal_type = request.form["meal_type"]
    company = request.form["company"]
    diet = request.form["diet"]

    # Encode inputs
    encoded_input = [
        encoders["taste"].transform([taste])[0],
        encoders["budget"].transform([budget])[0],
        encoders["meal_type"].transform([meal_type])[0],
        encoders["company"].transform([company])[0],
        encoders["diet"].transform([diet])[0]
    ]

    prediction = model.predict([encoded_input])[0]

    result_row = data[data["dish"] == prediction].iloc[0]

    restaurant = result_row["restaurant"]
    price = result_row["price"]

    return render_template(
        "result.html",
        dish=prediction,
        restaurant=restaurant,
        price=price
    )

if __name__ == "__main__":
    app.run(debug=True)

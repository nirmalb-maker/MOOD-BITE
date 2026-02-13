from flask import Flask, render_template, request
import pickle
import pandas as pd
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables
load_dotenv()

# Configure Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

# Initialize the client
client = genai.Client(api_key=api_key)

# Load ML model + encoders
try:
    model = pickle.load(open("model.pkl", "rb"))
    encoders = pickle.load(open("encoders.pkl", "rb"))
    data = pd.read_csv("data.csv")
except FileNotFoundError as e:
    raise FileNotFoundError(f"Required file not found: {e}")


@app.route("/")
def home():
    return render_template("index.html")


# ---------------------------
# ML Prediction + Compare Page
# ---------------------------

@app.route("/recommend", methods=["POST"])
def recommend():
    try:
        taste = request.form.get("taste")
        budget = request.form.get("budget")
        meal_type = request.form.get("meal_type")
        company = request.form.get("company")
        diet = request.form.get("diet")

        # Validate inputs
        if not all([taste, budget, meal_type, company, diet]):
            return "Error: All fields are required", 400

        # Encode inputs
        encoded_input = [
            encoders["taste"].transform([taste])[0],
            encoders["budget"].transform([budget])[0],
            encoders["meal_type"].transform([meal_type])[0],
            encoders["company"].transform([company])[0],
            encoders["diet"].transform([diet])[0]
        ]

        # Predict
        prediction = model.predict([encoded_input])[0]
        
        # Get result from data
        result_rows = data[data["dish"] == prediction]
        if result_rows.empty:
            return f"Error: Predicted dish '{prediction}' not found in database", 404
            
        result_row = result_rows.iloc[0]

        restaurant = result_row["restaurant"]
        base_price = int(result_row["price"])

        # Calculate delivery prices
        zomato_price = base_price + 20
        swiggy_price = base_price + 10

        return render_template(
            "compare.html",
            dish=prediction,
            restaurant=restaurant,
            base_price=base_price,
            zomato=zomato_price,
            swiggy=swiggy_price
        )

    except KeyError as e:
        return f"Error: Missing encoder or column - {e}", 500
    except Exception as e:
        return f"Error: {str(e)}", 500


# ---------------------------
# Final Result Page
# ---------------------------

@app.route("/final", methods=["POST"])
def final():
    dish = request.form.get("dish", "Unknown")
    restaurant = request.form.get("restaurant", "Unknown")
    price = request.form.get("price", "0")

    return render_template(
        "result.html",
        dish=dish,
        restaurant=restaurant,
        price=price,
        ai_response=None
    )


# ---------------------------
# AI MODE (Gemini)
# ---------------------------

@app.route("/ai_mode", methods=["POST"])
def ai_mode():
    try:
        dish = request.form.get("dish", "Unknown")
        restaurant = request.form.get("restaurant", "Unknown")
        price = request.form.get("price", "0")

        prompt = f"""
A user selected this dish recommendation:

Dish: {dish}
Restaurant: {restaurant}
Price: ₹{price}

Explain why this dish suits their mood and preferences.
Make it friendly, personalized, and slightly premium tone.
Also suggest one small add-on recommendation.
Keep it under 150 words.
"""

        # Use the new API with correct model name
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        
        ai_text = response.text
        print("AI Response:", ai_text)

        return render_template(
            "result.html",
            dish=dish,
            restaurant=restaurant,
            price=price,
            ai_response=ai_text
        )

    except Exception as e:
        print(f"AI Mode Error: {str(e)}")
        return render_template(
            "result.html",
            dish=request.form.get("dish", "Unknown"),
            restaurant=request.form.get("restaurant", "Unknown"),
            price=request.form.get("price", "0"),
            ai_response=f"AI service temporarily unavailable. Error: {str(e)}"
        )


if __name__ == "__main__":
    app.run(debug=True)
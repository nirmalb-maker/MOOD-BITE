from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
from google import genai
from dotenv import load_dotenv
import os

app = Flask(__name__)


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=api_key)


model = pickle.load(open("model.pkl", "rb"))
encoders = pickle.load(open("encoders.pkl", "rb"))
data = pd.read_csv("data.csv")



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():
    try:
        taste = request.form.get("taste")
        budget = request.form.get("budget")
        meal_type = request.form.get("meal_type")
        company = request.form.get("company")
        diet = request.form.get("diet")

        print("Taste:", taste)
        print("Budget:", budget)
        print("Meal Type:", meal_type)
        print("Company:", company)
        print("Diet:", diet)


        # Encode input
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
        base_price = int(result_row["price"])

        
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

    except Exception as e:
        print(e)
        return f"Error in recommendation: {str(e)}"



@app.route("/final", methods=["POST"])
def final():

    dish = request.form.get("dish")
    restaurant = request.form.get("restaurant")
    price = request.form.get("price")

    prompt = f"""
Explain why {dish} from {restaurant} at price ₹{price} is a good choice for the user. Keep it under 100 words.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        ai_text = response.text

    except Exception as e:
        return jsonify({"response": f"AI Error: {str(e)}"})


    return render_template(
        "result.html",
        dish=dish,
        restaurant=restaurant,
        price=price,
        ai_response=ai_text
    )



@app.route("/chat_ai", methods=["POST"])
def chat_ai():

    user_text = request.form.get("user_text")

    if not user_text:
        return jsonify({"response": "Please describe your food preferences."})

    prompt = f"""
User request:
"{user_text}"

Based on this description:
- Recommend a dish
- Suggest restaurant type
- Explain why it suits them

Keep it under 150 words.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        ai_text = response.text
        return jsonify({"response": ai_text})

    except Exception as e:
        return jsonify({"response": f"AI Error: {str(e)}"})



if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

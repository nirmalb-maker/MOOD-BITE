# MoodBite  
## Intelligent Food Recommendation System  

---

# PART I — SYSTEM OVERVIEW & ARCHITECTURE

---

## 1. Introduction

MoodBite is a web-based food recommendation system designed to generate structured and deterministic dish suggestions based on user preferences.

The system is primarily powered by a supervised Machine Learning model (Decision Tree Classifier). An optional AI layer is integrated to provide contextual explanation and conversational interaction, but the core recommendation logic remains ML-driven and explainable.

This project demonstrates:

- Practical ML model deployment in a web application
- Clear separation between structured ML logic and optional AI assistance
- Modular backend architecture
- Deterministic recommendation behavior

---

## 2. System Objective

Food recommendation systems typically rely on:

- Static rule-based filtering  
or  
- Heavy generative AI without structured logic  

MoodBite combines structured ML classification with optional AI reasoning, ensuring:

- Predictable output  
- Explainable model behavior  
- Minimal dependency on generative systems  
- Clean architectural separation  

---

## 3. Core Functional Modules

### 3.1 Structured ML Recommendation Engine (Primary System)

Users provide structured inputs:

- Taste (Spicy / Sweet)
- Budget (Low / Medium / High)
- Meal Type (Snack / Heavy)
- Company (Alone / Group)
- Diet (Healthy / Junk)

The system:

1. Encodes categorical inputs
2. Passes them to a trained `DecisionTreeClassifier`
3. Predicts a suitable dish
4. Retrieves associated restaurant and pricing data

This ensures deterministic and explainable recommendations.

---

### 3.2 Restaurant Comparison Module

After prediction, the system displays:

- Recommended dish
- Restaurant details
- Simulated pricing comparison (Swiggy vs Zomato)
- Highlighted best option

This simulates real-world decision-making context without relying on external APIs.

---

### 3.3 Optional AI Insight Layer

An additional AI mode allows users to:

- Enter free-text food preferences
- Use voice input (browser-supported)
- Receive contextual explanation or alternative suggestions

Important:

AI does not replace ML prediction.  
It serves only as an assistive layer to enhance user experience.

---

## 4. System Architecture

Application flow:

Frontend (HTML/CSS/JS)  
        ↓  
Flask Backend  
        ↓  
Machine Learning Model (Decision Tree)  
        ↓  
Dataset Lookup Layer  
        ↓  
Optional AI Insight Layer  

Design Principles:

- ML-first architecture  
- AI as enhancement, not replacement  
- Modular Flask routes  
- Clean separation of concerns  
- Minimal external dependency  

---

## 5. Technology Stack

Backend:
- Python
- Flask

Machine Learning:
- Scikit-learn
- Pandas
- LabelEncoder

Frontend:
- HTML
- CSS
- JavaScript

Optional AI Layer:
- Google Gemini API

Voice Input:
- Web Speech API

---

# PART II — IMPLEMENTATION & USAGE

---

## 6. Project Structure

```
MOODBITE/
│
├── app.py               # Flask application
├── train.py             # Model training script
├── data.csv             # Dataset
├── model.pkl            # Trained ML model
├── encoders.pkl         # Encoders for categorical features
├── requirements.txt     # Dependencies
│
├── templates/
│   ├── index.html       # Landing page
│   ├── compare.html     # Comparison page
│   └── result.html      # Final recommendation page
│
└── static/
    └── style.css        # UI styling
```

---

## 7. Installation Guide

### Step 1 — Clone Repository

```bash
git clone https://github.com/yourusername/MOOD-BITE.git
cd MOOD-BITE
```

---

### Step 2 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 3 — Configure Environment Variables

Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your_api_key_here
```

Note:  
The AI layer is optional. The core ML system functions independently.

---

### Step 4 — Train Model (Optional)

```bash
python train.py
```

---

### Step 5 — Run Application

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 8. Screenshots

---

### Landing Page

<img width="812" height="838" alt="Screenshot 2026-02-14 074738" src="https://github.com/user-attachments/assets/37974f7c-bd1c-478a-bfab-c4c7faaaf10f" />
<img width="1862" height="867" alt="Screenshot 2026-02-14 074632" src="https://github.com/user-attachments/assets/525781c5-c280-440b-8f0c-f9e9430e0224" />


Description:  
Structured input interface for ML-based recommendation.

---

### Comparison Page

<img width="1697" height="842" alt="Screenshot 2026-02-14 075346" src="https://github.com/user-attachments/assets/66b2e590-a98b-4ace-9e4e-a056735096be" />


Description:  
Displays recommended dish with simulated pricing comparison.

---

### Final Recommendation Page

<img width="710" height="613" alt="Screenshot 2026-02-14 075405" src="https://github.com/user-attachments/assets/252a8ad9-fda7-404f-9ae8-3fe7746524a5" />


Description:  
Shows predicted dish and restaurant details.

---

### AI Mode Panel

<img width="1406" height="725" alt="Screenshot 2026-02-14 074824" src="https://github.com/user-attachments/assets/42f0d1a9-82af-456a-b682-7a121b3bce11" />


Description:  
Optional conversational interface for natural language input.

---

## 9. Dataset Overview

The dataset includes:

- taste
- budget
- meal_type
- company
- diet
- dish
- restaurant
- price

The model predicts `dish` based on encoded categorical inputs.

---

## 10. Model Selection Rationale

DecisionTreeClassifier was selected because:

- Handles categorical data effectively
- Requires minimal preprocessing
- Produces deterministic output
- Easy to interpret
- Suitable for small structured datasets

---

## 11. Limitations

- Limited dataset size
- Simulated delivery pricing
- No real-time API integration
- No persistent user history
- AI usage limited by free-tier API quota

---

## 12. Future Enhancements

- Expanded dataset
- Real delivery API integration
- Model performance evaluation metrics
- User authentication system
- Recommendation history storage
- Cloud deployment

---

## 13. Conclusion

MoodBite demonstrates how a structured ML-based system can be deployed in a web environment and optionally enhanced with a conversational AI layer, while maintaining architectural clarity and deterministic core behavior.

The project emphasizes modular design, explainable ML logic, and controlled AI usage.

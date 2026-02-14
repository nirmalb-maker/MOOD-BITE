<p align="center">
  <img src="./img.png" alt="MoodBite Banner" width="100%">
</p>

# MoodBite 🍽️🎯  
## Intelligent ML-Based Food Recommendation System  

---

## 📌 Basic Details

### 👥 Team Name  
**Delulu**

### 👤 Team Members
- Nirmal B Chacko – RIT KOTTAYAM  
- Jolsina U – RIT KOTTAYAM

---

### 🌐 Hosted Project Link  
🔗 https://mood-bite.onrender.com  

---

## 🧠 Project Description  

MoodBite is a structured Machine Learning–driven food recommendation system that generates deterministic dish suggestions based on user preferences such as taste, budget, meal type, company, and diet.

The system is powered by a **Decision Tree Classifier** and optionally enhanced with an AI insight layer for conversational interaction — while keeping ML logic as the core engine.

---

## ❓ The Problem Statement  

Food recommendation platforms typically rely on:

- Static rule-based filtering (limited intelligence)  
OR  
- Fully generative AI systems (non-deterministic & non-explainable)

Users receive unpredictable suggestions without structured reasoning.

---

## ✅ The Solution  

MoodBite combines:

- Supervised ML (DecisionTreeClassifier)
- Encoded categorical input processing
- Deterministic prediction logic
- Structured restaurant lookup
- Simulated price comparison
- Optional conversational AI enhancement

This ensures:

✔ Predictable Output  
✔ Explainable ML Logic  
✔ Clean Modular Architecture  
✔ Controlled AI Usage  

---

# ⚙ Technical Details

## 💻 Technologies Used

### 🔹 Languages
- Python
- HTML
- CSS
- JavaScript

### 🔹 Framework
- Flask

### 🔹 Libraries
- Scikit-learn
- Pandas
- LabelEncoder
- Pickle
- python-dotenv

### 🔹 Deployment
- Render (Cloud Hosting)

### 🔹 Optional AI
- Google Gemini API

---

# 🚀 Features

- ML-Based Dish Prediction
- Decision Tree Classifier Model
- LabelEncoder-based categorical encoding
- Restaurant recommendation system
- Simulated Swiggy vs Zomato pricing comparison
- Optional AI conversational mode
- Voice Input (Web Speech API)
- Modular Flask backend
- Deterministic & explainable logic

---

# 🛠 Implementation

## 🔹 Installation

```bash
git clone https://github.com/yourusername/MOOD-BITE.git
cd MOOD-BITE
pip install -r requirements.txt
```

## 🔹 Train Model (Optional)

```bash
python train.py
```

## 🔹 Run Application

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---


# 📸 Project Screenshots

---

## 1️⃣ Landing Page – Structured ML Input

<img width="812" height="838" alt="Screenshot 2026-02-14 074738" src="https://github.com/user-attachments/assets/858c3520-5c1c-49f4-8820-8e321559186c" />scription:** 
<img width="1862" height="867" alt="Screenshot 2026-02-14 074632" src="https://github.com/user-attachments/assets/1a3f3b4d-b481-4dbf-a866-a8b6876b39c6" />

User selects taste, budget, meal type, company, and diet.  
Inputs are encoded and passed to the Decision Tree model.

---

## 2️⃣ Comparison Page – Price Evaluation

<img width="1697" height="842" alt="Screenshot 2026-02-14 075346" src="https://github.com/user-attachments/assets/cbf8b421-172f-468f-bc40-8e370d047cb9" />


**Description:**  
Displays predicted dish, restaurant details, and simulated Swiggy vs Zomato pricing with best option highlighted.

---

## 3️⃣ Final Recommendation – ML Output

<img width="710" height="613" alt="Screenshot 2026-02-14 075405" src="https://github.com/user-attachments/assets/d6eaf204-f821-41c6-8eee-3b842f6e4164" />


**Description:**  
Shows deterministic dish prediction with restaurant and base price.

---

## 4️⃣ AI Mode Panel – Optional Insight Layer

<img width="1406" height="725" alt="Screenshot 2026-02-14 074824" src="https://github.com/user-attachments/assets/d53a8636-7ccc-4cdd-8041-aa4d46164a5b" />

**Description:**  
Free-text and voice-based interaction.  
Enhances UX without replacing ML logic.


## 🏠 Landing Page

<p align="center">
  <img src="https://github.com/user-attachments/assets/37974f7c-bd1c-478a-bfab-c4c7faaaf10f" width="80%">
</p>

Structured user interface for ML-based preference input.

---

## 📊 Comparison Page

<p align="center">
  <img src="https://github.com/user-attachments/assets/66b2e590-a98b-4ace-9e4e-a056735096be" width="80%">
</p>

Displays predicted dish with simulated Swiggy vs Zomato pricing.

---

## 🍽 Final Recommendation Page

<p align="center">
  <img src="https://github.com/user-attachments/assets/252a8ad9-fda7-404f-9ae8-3fe7746524a5" width="60%">
</p>

Shows dish prediction, restaurant details, and pricing.

---

## 🤖 AI Mode Panel

<p align="center">
  <img src="https://github.com/user-attachments/assets/42f0d1a9-82af-456a-b682-7a121b3bce11" width="80%">
</p>

Conversational interface for contextual food suggestions.

---

# 🧩 System Architecture

```
Frontend (HTML/CSS/JS)
        ↓
Flask Backend
        ↓
DecisionTreeClassifier (ML Model)
        ↓
Dataset Lookup Layer
        ↓
Optional AI Insight Layer
```

### Architecture Principles

- ML-first design
- AI as enhancement, not replacement
- Modular Flask routes
- Clean separation of concerns
- Deterministic output generation

---

# 🔄 Application Workflow

1. User selects structured preferences  
2. Input encoded via LabelEncoder  
3. DecisionTreeClassifier predicts dish  
4. Dataset lookup retrieves restaurant + price  
5. Simulated price comparison generated  
6. Optional AI explanation displayed  

---

# 📡 API Documentation

### Base URL
```
https://mood-bite.onrender.com
```

---

## 🔹 POST /predict

### Description
Predicts dish based on structured preferences.

### Form Parameters

- taste
- budget
- meal_type
- company
- diet

### Response

- dish
- restaurant
- price

---

## 🔹 POST /compare

### Description
Generates Swiggy vs Zomato price comparison.

### Request

- dish
- price

### Response

- Swiggy Price
- Zomato Price
- Best Platform

---

# 🎥 Project Demo

### 🌐 Live Site
https://mood-bite.onrender.com  

### 🎬 Demo Video
(Add YouTube / Drive link here)

---

# 🤖 AI Tools Used (Transparency)

**Tool Used:** ChatGPT  

**Purpose:**
- Documentation formatting
- Backend structure assistance
- ML architecture refinement
- Debugging suggestions

**Estimated AI Contribution:** ~30–40%

**Human Contributions:**
- Architecture design
- ML model logic
- Dataset preparation
- Deployment setup
- Frontend integration
- Testing & validation

---

# 👥 Team Contributions

### Nirmal B Chacko
- ML Model Development
- Backend Architecture
- Documentation Lead
- Deployment Configuration
- System Design & Planning

### [Teammate Name]
- Frontend Development
- UI Styling
- Integration Testing
- Feature Implementation

---

# 📜 License

Licensed under the MIT License.

---

Made with ❤️ at TinkerHub 🚀

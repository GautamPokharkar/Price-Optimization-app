# 📊 Price Optimization ML System – Machine Learning Application

A **machine learning–driven pricing optimization system** built using **Flask, XGBoost, and Pandas** to recommend **profit-maximizing product prices** based on historical sales data, competitor pricing, and business constraints.

---

## ✅ Key Features

- Predicts **optimal product pricing** using supervised machine learning  
- Incorporates **cost price, competitor price, and historical demand patterns**  
- Uses a trained **XGBoost regression model** for demand prediction  
- Applies **constrained optimization** to ensure realistic pricing recommendations  
- Provides both **API-based and UI-based interaction** for price simulation  

---

## 🧠 Model & Optimization Logic

- **Model:** XGBoost Regressor  
- **Prediction Target:** Quantity sold  

### Profit Objective
Profit = (Price − Cost) × Predicted Quantity

The system evaluates multiple pricing scenarios and selects the price that **maximizes expected profit** under defined constraints.

### Input Features
- UnitPrice  
- CompetitorPrice  
- Previous Month Price  
- Previous Month Quantity  
- Average & Standard Deviation of Price  
- Average & Standard Deviation of Quantity  
- Weekend Indicator  
- Total Historical Quantity  

---

## 🧪 Application Workflow

1. User provides pricing and market inputs  
2. ML model predicts expected demand  
3. Profit is calculated across candidate prices  
4. Optimal price is selected  
5. Results are returned via UI or API  

---

## ⚙️ Setup & Execution

```bash
# 1. Clone the repository
git clone https://github.com/your-username/price-optimizer
cd price-optimizer

# 2. Create virtual environment
python -m venv env

# 3. Activate environment
# Windows
.\env\Scripts\activate
# macOS/Linux
source env/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the application
python app.py

🧰 Tech Stack

Language: Python

Backend Framework: Flask

Machine Learning: XGBoost

Data Processing: Pandas

Frontend: HTML, Jinja2, CSS

🎯 Learning Outcomes

Built an end-to-end machine learning system from data preprocessing to deployment

Applied regression-based demand forecasting for pricing decisions

Designed a profit optimization strategy using ML predictions

Integrated ML models into a production-style backend application

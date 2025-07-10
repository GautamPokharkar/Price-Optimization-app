# 📊 Price Optimization ML App (Flask + XGBoost)

A minimal machine learning web app built with **Flask**, **XGBoost**, and **Pandas**, designed to recommend the optimal product price to maximize profit based on historical data and business constraints.

---

## ✅ Features

- 🧠 Predicts optimal price for a product using ML
- 💰 Takes into account cost price, competitor price & past sales
- 📊 Real-time input with API or UI form
- 🔄 Constrained optimization for realistic pricing
- 🧪 Includes a trained XGBoost regression model

---

## ⚙️ Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/your-username/price-optimizer
cd price-optimizer

# 2. Create a virtual environment
python -m venv env

# 3. Activate it
# On Windows:
.\env\Scripts\activate
# On macOS/Linux:
source env/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the app
python app.py
🧠 Model Details
Model: XGBoost Regressor

Target: Predict quantity sold

Objective: Maximize profit
Profit = (Price - Cost) × Predicted Quantity

Features used:

UnitPrice

CompetitorPrice

PrevMonthQuantity

PrevMonthPrice

AvgQuantity, QuantityStd

AvgPrice, PriceStd

IsWeekend

TotalQuantity

🧰 Tech Stack
[Flask] - Backend web server

[Pandas] - Data handling

[XGBoost] - Machine learning model

[HTML + Jinja2] - Frontend templates

🏁 Result
Interactive UI + API to simulate business pricing scenarios and generate data-driven pricing strategies.


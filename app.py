import os
import pickle
import pandas as pd
from flask import Flask, render_template, request, jsonify
from utils import constrained_optimal_price

app = Flask(__name__)

BASE = os.path.dirname(__file__)

# Load your trained model
with open(os.path.join(BASE, 'model.pkl'), 'rb') as f:
    model = pickle.load(f)

# Load processed model data (must contain 'StockCode', 'Year', 'Month' and all feature columns)
data_path = os.path.join(BASE, 'model_data.pkl')
try:
    model_df = pd.read_pickle(data_path)
except Exception:
    import joblib
    model_df = joblib.load(data_path)

# If someone pickled a tuple accidentally, extract the DataFrame
if isinstance(model_df, tuple):
    dfs = [x for x in model_df if isinstance(x, pd.DataFrame)]
    if not dfs:
        raise RuntimeError("model_data.pkl did not contain a DataFrame")
    model_df = dfs[0]

if 'StockCode' not in model_df.columns:
    raise RuntimeError("model_data.pkl must contain a 'StockCode' column")

@app.route('/')
def home():
    stock_codes = sorted(model_df['StockCode'].unique().tolist())
    return render_template('index.html', stock_codes=stock_codes)

@app.route('/api/optimize', methods=['POST'])
def optimize():
    payload = request.json
    product_id       = payload.get('product_id')
    unit_price       = float(payload.get('unit_price', 0))
    competitor_price = float(payload.get('competitor_price', 0))
    cost_price       = float(payload.get('cost_price', 0))
    is_weekend       = int(payload.get('is_weekend', 0))
    total_quantity   = int(payload.get('total_quantity', 0))

    # Validate product exists
    df_prod = model_df[model_df['StockCode'] == product_id]
    if df_prod.empty:
        return jsonify({'error': f"Product '{product_id}' not found"}), 400

    # Use most recent row for historical stats
    latest = df_prod.sort_values(['Year', 'Month']).iloc[-1]

    # Build feature dict exactly as model expects
    features = {
        'UnitPrice': unit_price,
        'CompetitorPrice': competitor_price,
        'PrevMonthQuantity': latest['PrevMonthQuantity'],
        'PrevMonthPrice':    latest['PrevMonthPrice'],
        'IsWeekend':         is_weekend,
        'TotalQuantity':     total_quantity,
        'AvgQuantity':       latest['AvgQuantity'],
        'QuantityStd':       latest['QuantityStd'],
        'AvgPrice':          latest['AvgPrice'],
        'PriceStd':          latest['PriceStd']
    }

    # Run optimization
    result = constrained_optimal_price(model, features, cost_price)
    result['product_id'] = product_id
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

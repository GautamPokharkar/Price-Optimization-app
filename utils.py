import numpy as np
import pandas as pd

def find_optimal_price(model, base_features, cost_price,
                       price_range=(0.1, 100), n_points=50):
    prices = np.linspace(price_range[0], price_range[1], n_points)
    profits = []

    for p in prices:
        temp = base_features.copy()
        temp['UnitPrice'] = p
        temp['PriceRatio'] = p / temp['CompetitorPrice']
        temp['PriceZScore'] = (p - temp['AvgPrice']) / (temp['PriceStd'] + 1e-6)

        df_in = pd.DataFrame([temp])[model.feature_names_in_]
        demand = model.predict(df_in)[0]
        profits.append((p - cost_price) * demand)

    idx = int(np.argmax(profits))
    return prices[idx], profits[idx], (prices.tolist(), profits)

def constrained_optimal_price(model, features, cost_price):
    opt_price, max_profit, (all_prices, all_profits) = find_optimal_price(
        model, features, cost_price
    )
    return {
        'optimal_price': round(opt_price, 2),
        'max_profit':    round(max_profit, 2),
        'price_profit_curve': {
            'prices':  all_prices,
            'profits': all_profits
        }
    }

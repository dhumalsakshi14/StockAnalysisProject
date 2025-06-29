import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json

# Load the CSV file
data_file = '/mnt/data/sample_data.csv'
df = pd.read_csv(data_file)

# Ensure the date column is parsed correctly if present
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

# Assume 'Close' is the column representing stock price
if 'Close' in df.columns:
    df['Moving_Avg_20'] = df['Close'].rolling(window=20).mean()
    df['Moving_Avg_50'] = df['Close'].rolling(window=50).mean()

    highest_price = df['Close'].max()
    lowest_price = df['Close'].min()
    volatility = df['Close'].std()

    # Generate the plot
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Close'], label='Closing Price', color='blue')
    plt.plot(df.index, df['Moving_Avg_20'], label='20-day Moving Avg', linestyle='dashed', color='red')
    plt.plot(df.index, df['Moving_Avg_50'], label='50-day Moving Avg', linestyle='dashed', color='green')
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.title('Stock Price Trends')
    plt.legend()
    plt.grid()

    # Save the plot
    plt.savefig('/mnt/data/stock_price_trends.png')
    plt.show()

    # Prepare JSON output
    analysis_results = {
        "highest_price": highest_price,
        "lowest_price": lowest_price,
        "volatility": volatility,
        "moving_avg_20": df['Moving_Avg_20'].dropna().tolist(),
        "moving_avg_50": df['Moving_Avg_50'].dropna().tolist()
    }

    with open('/mnt/data/analysis_results.json', 'w') as json_file:
        json.dump(analysis_results, json_file, indent=4)

    print("Analysis complete. Check the generated files:")
    print("- Stock price trend plot: /mnt/data/stock_price_trends.png")
    print("- Analysis results JSON: /mnt/data/analysis_results.json")
else:
    print("Error: 'Close' column not found in the dataset.")

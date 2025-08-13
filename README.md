# Spread Option Pricing for Power Transmission Rights

This project explores how to value cross-border electricity transmission rights in European power markets using financial spread options. The goal is to determine how much a trader should pay for transmission capacity between countries (e.g., Germany and France), based on expected price spreads and volatility.

## Objectives

- Understand transmission capacity as a financial asset

- Implement Kirk’s approximation and Monte Carlo simulation to price spread options

- Use real power market data (e.g., France and GB day-ahead prices)

- Create clean, reproducible analysis in Python notebooks

## Why This Matters

In real markets, traders bid for interconnection rights. The value of these rights depends on the price spread between regions. Spread options are a powerful way to model this economically.

# Explain why GB-France 
- link to brexit, wider and more persistent spreads, high volatility (UK power system is more weather-dependent due to weather sensitivity)

## Project Structure
notebooks/           # All exploratory and modeling notebooks
data/
├── raw/           # Original source data 
└── processed/     # Cleaned or enriched data
utils/               # Reusable pricing functions (Kirk, Monte Carlo)
outputs/
├── charts/        # Final plots and figures
└── results/       # Output values or logs

## Requirements
- Python 3.10+
- pandas, numpy, scipy, matplotlib, seaborn, requests, jupyter
Install with bash:
pip install -r requirements.txt




-----------------------
## Next Steps for a production ready signal
1. Integrate execution contraints
a.) Capacity limits - apply max flow caps (e.g., 2GW) to ensure PnL reflects the physical limits of the UK-France interconnector
b.) Transaction costs - subtract bid/offer spreads, clearing fees, and estimated slippage to calculate net returns.
c.) Outage filters - exclude hours where interconnector availability is reduced or zero due to maintenance or unplanned faults.

2.) Build a no leak backtest with decision rules
a.) No leak parameter estimation - When calculating volatilities, correlations, or model inputs, only use data available before the trade date - avoid using data in the future
b.) Equity curve output - produce a cumulative PnL chart to visualise consistency, drawdowns, and regime performance.
c.) Define rules - such as clear entry/exit conditions based on valuation minus costs and capacity availability.


Summary - Make it tradable (3):
1. Pull 5+ years of real UK and France day-ahead prices so we can stress-test across different market regimes, especially 2022.
2. Reflect reality - Cap flows at interconnector limits, deduct transaction costs, skip hours when capacity is offline.
3. Build a no-leak backtest that produces an equity curve and decision rule for when to switch the strategy on or off.


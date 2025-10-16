# UK–France Power Spread Option Pricing  
**Valuing Transmission Rights via Kirk’s Approximation and Monte Carlo Simulation**

*Author: Lyndon Odia*
*Project Status: Completed*

## Overview
This project values **UK–France interconnector transmission capacity** by treating it as a **spread option** between the UK (simulated) and France (ENTSO-E) day-ahead power prices.  
Using both **Kirk’s analytical approximation** and **Monte Carlo simulation**, we estimate the fair value of the right to flow power between markets, incorporating *real market volatility, correlation, and capacity costs* from **JAO monthly auctions**.

## Objective:
- Quantify the fair €/MWh value of UK↔FR transmission optionality.
- Compare Kirk’s closed-form approximation with Monte Carlo simulation.
- Integrate *capacity cost* (from JAO auctions) as strike (K).
- Analyse sensitivity to volatility, correlation, and expiry.

## Project Structure


power-spread-option-pricing-main/

│

├── data/

│   ├── raw/                     # ENTSO-E & simulated inputs

│   └── processed/               # Cleaned hourly merged dataset

│

├── notebooks/

│   ├── 01_intro_and_objective.ipynb

│   ├── 02_data_collection.ipynb

│   ├── 03_eda_spread_analysis.ipynb

│   ├── 04_kirk_model.ipynb

│   ├── 05_monte_carlo_simulation.ipynb

│   └── 06_sensitivity_analysis.ipynb

│

├── docs/

│   ├── figures/                 # Key visuals & sensitivity plots

│   └── executive_summary.pdf

│

└── config.py

│

└── presentation.pptx
 

## Methodology
| Step | Description | Output |
|------|--------------|--------|
| 1️ | **Data Collection** – FR via ENTSO-E API (A44), UK via simulated CSV. | Hourly merged dataset |
| 2️ | **Data Cleaning** – Align timestamps, convert GBP→EUR (FX = 1.17), check for missing hours (213 gaps). | `UK_FR_day_ahead_hourly_merged_spread.csv` |
| 3️ | **EDA** – Compute spread distribution, volatility, correlation. | `03_eda_spread_analysis.ipynb` |
| 4️ | **Kirk’s Approximation** – Closed-form spread option pricing. | `04_kirk_model.ipynb` |
| 5️ | **Monte Carlo Simulation** – 100k GBM paths for UK & FR prices. | `05_monte_carlo_simulation.ipynb` |
| 6️ | **Sensitivity Analysis** – Volatility, correlation, expiry. | `06_sensitivity_analysis.ipynb` |


## Base Case Inputs (Jan–Jul 2025)
| Parameter | Description | Value |
|------------|--------------|--------|
| S₁ | UK mean price (N2EX, EUR/MWh) | **81.104** |
| S₂ | FR mean price (ENTSO-E, EUR/MWh) | **68.064** |
| σ₁ | UK annualised volatility | **0.198** |
| σ₂ | FR annualised volatility | **1.008** |
| ρ | Correlation (UK–FR) | **0.142** |
| T | Time to expiry | **1/12 years (1 month)** |
| K | Capacity cost (strike) | **€0.76/MWh** |
| FX | GBP→EUR conversion | **1.17** |


## Model Frameworks
### 1. Kirk’s Approximation (Analytical)
### 2. Monte Carlo Simulation (100,000 paths)
Monte Carlo average of payoffs = Fair option value.


## Results Summary
| Model | Option Value (€/MWh) | Interpretation |
|--------|----------------------|----------------|
| Kirk’s Approximation | **16.00** | Analytical closed-form estimate |
| Monte Carlo Simulation | **15.99** | Numerical validation (100k paths) |
| Average Spread | **13.04** | Mean of (UK – FR) prices |
| Capacity Cost (K) | **0.76** | From JAO GB→FR auctions |
| **Net Option Value** | **≈ €16.00/MWh** | Fair value **after capacity cost already included in payoff** |
| **1 GW × 720h** | **≈ €11.52m/month** | Implied interconnector notional value |

 *Both models converge closely, validating the assumptions and confirming the robustness of the analytical approximation.*

 > **Note:** The strike \(K = €0.76/MWh\) is embedded inside both models’ payoff (\(\max(S_1 − S_2 − K, 0)\)).  
> Therefore, the reported €16.0/MWh is **net of the capacity cost**.  
> The €0.76/MWh auction price represents an *upfront premium* that traders pay for this optionality — not a further deduction.

 ## Sensitivity Insights
| Driver | Relationship | Observation |
|---------|---------------|--------------|
| **Volatility (σ)** | ↑ σ → ↑ Option Value | Convex payoff from uncertainty |
| **Correlation (ρ)** | ↑ ρ → ↓ Option Value | Convergent markets reduce spreads |
| **Expiry (T)** | ↑ T → ↑ Option Value | More time = more optionality |
| **Capacity Cost (K)** | ↑ K → ↓ Value | Linear cost offset effect |
See `/docs/figures/` for plots:
- Volatility Sensitivity → *Value vs σ*
- Correlation Sensitivity → *Value vs ρ*
- Expiry Sensitivity → *Value vs T*


## Interpretation
- The **raw spread** (~€13/MWh) reflects the *average price difference*.
- The **option value** (~€16/MWh) captures the *right to flow only when profitable* — ignoring negative spreads.
- The **capacity cost** (€0.76/MWh) represents the *market-clearing price* paid to acquire that right (from JAO explicit auctions).
- The small positive gap between **option value** and **mean spread** demonstrates how **volatility, correlation, and flexibility** drive real economic value.
> “Optionality converts volatility into opportunity — and that’s what interconnector traders pay for.”

##  Reproducibility
1. Clone this repository  
```bash
git clone https://github.com/lo-devx/power-spread-option-pricing-main.git
cd power-spread-option-pricing-main
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Run notebooks in order (01_ → 06_).
4. Outputs and figures saved to /docs/figures/ and /outputs/.



## Limitations & Future Enhancements
Area Current Enhancement
- Exercise Style European monthly Hourly simulation (American style)
- Volatility Static (historical) Stochastic / regime-switching vols
- Correlation Fixed Time-varying correlation (DCC-GARCH)
- Costs No transaction/imbalance Include balancing, losses, fees
- Directionality GB->FR only Add FR->GB asymmetry
- Pull 5+ years of real UK and France day-ahead prices so we can stress-test across different market regimes, especially 2022.
- Reflect reality - Cap flows at interconnector limits, deduct transaction costs, skip hours when capacity is offline.

## Capacity Cost Reference
Source: Joint Allocation Office (JAO)
Border: IF2-GB → FR
Period: Jan–Jul 2025 (monthly base auctions)
Average clearing price: €0.76/MWh

### References
1. Kirk, E. (1995). “Correlation in the Energy Markets: Spread Option Valuation.”
2. Hull, J. (2017). Options, Futures, and Other Derivatives.
3. ENTSO-E Transparency Platform
4. Joint Allocation Office (JAO) Auction Results Portal.
5. Black–Scholes, F. (1973). “The Pricing of Options and Corporate Liabilities.”

## Power Trading & Fundamentals
| Area | Resource | Description |
|-------|-----------|-------------|
| **European Power Data** | [ENTSO-E Transparency Platform](https://transparency.entsoe.eu/) | Official EU data source for day-ahead, intraday, generation, and cross-border flows. |
| **UK Power Market** | [National Grid ESO Data Portal](https://data.nationalgrideso.com/) | Real-time UK grid data: demand, generation mix, interconnector flows, and balancing. |
| **Capacity Auctions** | [Joint Allocation Office (JAO)](https://www.jao.eu/auctions) | Source for interconnector capacity auctions and clearing prices (PTR/FTR). |
| **Market Monitoring & Policy** | [Ofgem – Market Insights](https://www.ofgem.gov.uk/energy-data-and-research) | UK market design, regulation, and interconnector updates. |
| **Price & Market News** | [Montel Online](https://www.montelnews.com/) | European power, gas, and carbon news and forward price commentary. |
| **Transmission & Interconnectors** | [ENTSO-E System Development Reports](https://www.entsoe.eu/outlooks/) | Insights into cross-border capacity planning and future interconnector projects. |
| **Educational / Learning** | [EEX Academy (European Energy Exchange)](https://www.eex.com/en/academy) | Short online courses on power and gas trading basics. |




### Communications
[Presentation Deck (Download powerpoint deck)](docs/lyndon_odia_power_spread_option_pricing.pdf)

### Contact
Lyndon Odia | lynodia@outlook.com


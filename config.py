
from datetime import datetime, timedelta

#Define directories
raw_data_dir = "/Users/Lyndon.Odia/Desktop/sede-test/power-spread-option-pricing/data/raw"
processed_data_dir = "/Users/Lyndon.Odia/Desktop/sede-test/power-spread-option-pricing/data/processed"

# Define time range - 7 months 
START_DATE = datetime(2025, 1, 1, 0, 0)
END_DATE = datetime(2025, 8, 1, 23, 0)

#FX
FX_GBP_EUR = 1.17

#Define API keys 
API_KEY = "3faef1ee-b130-4678-9759-4ac9c0af0941"  

#Define bidding zone for FR
FR_DOMAIN = "10YFR-RTE------C"
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

#Define directories
raw_data_dir = "/Users/Lyndon.Odia/Desktop/lo-devx/power-spread-option-pricing-main/data/raw"
processed_data_dir = "/Users/Lyndon.Odia/Desktop/lo-devx/power-spread-option-pricing-main/data/processed"

# Define time range - 7 months 
START_DATE = datetime(2025, 1, 1, 0, 0)
END_DATE = datetime(2025, 8, 1, 23, 0)

#FX Conversion rates
FX_GBP_EUR = 1.17

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("ENTSOE_API_KEY")

#Define bidding zone for FR
FR_DOMAIN = "10YFR-RTE------C"


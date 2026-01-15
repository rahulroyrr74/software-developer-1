import pandas as pd
from sqlalchemy import create_engine
import logging
import time
import os

# Wait for PostgreSQL to start
time.sleep(10)

# Make sure logs folder exists
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("logs/app.log")
    ]
)

try:
    logging.info("Reading CSV file")
    df = pd.read_csv("uber_data.csv")

    logging.info("Cleaning data")
    df.dropna(inplace=True)

    logging.info("Connecting to PostgreSQL database")
    engine = create_engine("postgresql://postgres:admin@db:5432/uberdb")

    logging.info("Loading data into table 'uber_rides'")
    df.to_sql("uber_rides", engine, if_exists="replace", index=False)

    logging.info("Uber data loaded successfully ✅")

except Exception as e:
    logging.error(f"Error occurred: {e}")
    logging.info("Uber data loading failed ❌")
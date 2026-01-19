import pandas as pd
from sqlalchemy import create_engine
import time

# wait for postgres
time.sleep(10)

df = pd.read_csv("uber_data.csv")

engine = create_engine(
    "postgresql://postgres:admin@db:5432/uberdb"
)

df.to_sql("uber_rides", engine, if_exists="replace", index=False)

print("Data loaded successfully")

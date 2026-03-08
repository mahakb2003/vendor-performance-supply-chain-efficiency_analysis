import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

print("Script started")

# Configure logging
logging.basicConfig(
    filename='logs/ingestion_db.log',
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode='a'
)

engine = create_engine('sqlite:///inventory.db')


def ingest_db(df, table_name, engine):
    """Ingest dataframe into database table"""

    df.to_sql(
        table_name,
        con=engine,
        if_exists='replace',
        index=False
    )

    logging.info(f"Successfully ingested table: {table_name}")
    print(f"Inserted table: {table_name}")


def load_raw_data():
    """Load CSV files and ingest into database"""

    start = time.time()

    for file in os.listdir('data'):
        if '.csv' in file:
            df = pd.read_csv('data/' + file)
            logging.info(f'ingesting {file} in db')
            ingest_db(df, file[:-4], engine)

    end = time.time()
    total_time = (end - start) / 60

    logging.info("------------------ Ingestion Complete ------------------")
    logging.info(f"Total Time Taken: {total_time:.2f} minutes")

    print("Ingestion Complete")
    print(f"Total Time Taken: {total_time:.2f} minutes")


if __name__ == "__main__":
    load_raw_data()
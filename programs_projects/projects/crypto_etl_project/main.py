# ---------------------------------------------------------
# CRYPTO ETL PIPELINE
# ---------------------------------------------------------
#
# This script demonstrates a basic ETL (Extract, Transform,
# Load) pipeline.
#
# ETL means:
#
# E = Extract
#     Get raw data from an external source, such as an API.
#
# T = Transform
#     Clean, filter, or reshape the raw data.
#
# L = Load
#     Store the transformed data somewhere, such as a
#     database, CSV file, data warehouse, etc.
#
#
# Our pipeline:
#
#       Crypto API
#           |
#           v
#        EXTRACT
#           |
#           v
#       Raw JSON
#           |
#           v
#       TRANSFORM
#           |
#           v
#      Pandas DataFrame
#           |
#           v
#          LOAD
#           |
#           v
#      SQLite Database
#
# ---------------------------------------------------------




import os
import json
import sqlite3
import logging

import pandas as pd

# urllib.request is used to make HTTP requests to the API.
import urllib.request as ur

# HTTPError handles errors such as:
# 404 -> Not Found
# 401 -> Unauthorized
# 500 -> Server Error
#
# URLError handles problems such as:
# - No internet connection
# - Invalid URL
# - DNS problems
from urllib.error import HTTPError, URLError

# load_dotenv() loads environment variables from a .env file.
#
# This allows us to keep sensitive information such as
# API keys outside our Python source code.
from dotenv import load_dotenv


# ---------------------------------------------------------
# 0. LOGGING
# ---------------------------------------------------------
# logging is used instead of print() to show what
# is happening in our ETL pipeline.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s"
)


# ---------------------------------------------------------
# 1. EXTRACT
# ---------------------------------------------------------
# Get cryptocurrency data from the API.
def fetch_crypto_data(api_key):

    url = "https://api.coinlore.net/api/tickers/"

    logging.info(f"Connecting to API: {url}")

    try:
        # Create a request for the API.
        req = ur.Request(url)

        # Add the API key to the request header.
        req.add_header(
            "Authorization",
            f"Bearer {api_key}"
        )

        # Send the request and get the response.
        with ur.urlopen(req) as response:

            # Read the response and convert JSON text
            # into Python data (dictionary/list).
            parsed_data = json.loads(
                response.read().decode("utf-8")
            )

        # Return the data so the next ETL step can use it.
        return parsed_data

    except HTTPError as e:
        logging.error(
            f"HTTPError(fetch_crypto_data): {e.code}"
        )
        raise

    except URLError as e:
        logging.error(
            f"URLError(fetch_crypto_data): {e.reason}"
        )
        raise

    except Exception as e:
        logging.error(
            f"Exception(fetch_crypto_data): {e}"
        )
        raise


# ---------------------------------------------------------
# 2. TRANSFORM
# ---------------------------------------------------------
# Clean the API data and keep only the columns we need.
def transform_data(raw_json):

    logging.info("Transforming raw JSON with Pandas...")

    # Get the list of cryptocurrency records.
    coin_list = raw_json["data"]

    # Convert the JSON data into a Pandas DataFrame.
    df = pd.json_normalize(coin_list)

    # Keep only the columns we need.
    df_filtered = df[
        ["rank", "symbol", "name", "price_usd"]
    ]

    return df_filtered


# ---------------------------------------------------------
# 3. LOAD
# ---------------------------------------------------------
# Save the transformed data into a SQLite database.
def load_to_database(df, db_path):

    logging.info(
        f"Loading data into database at {db_path}..."
    )

    try:
        # Connect to the SQLite database.
        # If the database doesn't exist, SQLite creates it.
        with sqlite3.connect(db_path) as conn:

            # Save the DataFrame as a SQLite table.
            #
            # replace = replace the table if it already exists.
            # index=False = don't save the Pandas index as a column.
            df.to_sql(
                "live_crypto_prices",
                conn,
                if_exists="replace",
                index=False
            )

        logging.info(
            "Pipeline complete! Data loaded into SQLite."
        )

    except sqlite3.Error as e:
        logging.error(
            f"Database error occurred: {e}"
        )
        raise


# ---------------------------------------------------------
# 4. MAIN / ORCHESTRATION
# ---------------------------------------------------------
# main() controls the complete ETL pipeline:
#
# Extract → Transform → Load
def main():

    logging.info("Starting Crypto ETL Pipeline...")

    # Load variables from the .env file.
    load_dotenv()

    # Get the API key from the environment variable.
    my_api_key = os.getenv("COINCAP_API_KEY")

    # Stop the pipeline if the API key is missing.
    if not my_api_key:
        logging.error("API Key missing! Halting pipeline.")
        return

    try:
        # -------------------------
        # Extract
        # -------------------------
        raw_data = fetch_crypto_data(my_api_key)

        # -------------------------
        # Transform
        # -------------------------
        clean_df = transform_data(raw_data)

        # -------------------------
        # Load
        # -------------------------
        db_path = (
            "programs_projects\\projects\\"
            "crypto_etl_project\\crypto_data.db"
        )

        load_to_database(clean_df, db_path)

    except Exception as e:
        logging.critical(
            f"Pipeline failed: {e}"
        )


# ---------------------------------------------------------
# Run the pipeline
# ---------------------------------------------------------
# main() will run only when this file is executed directly.
if __name__ == "__main__":
    main()
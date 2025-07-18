import requests
import pandas as pd
import json
import os

API_URL = "https://jsonplaceholder.typicode.com/posts"
OUTPUT_DIR = "raw_data"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def extractDataFromSource(url):
    print(f"Extracting data from {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        print(f"Data extracted successfully. Total records: {len(data)}")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error extracting data from {url}: {e}")
        return None


def saveRawData(data, filename):
    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Data saved to {filepath}")

if __name__ == "__main__":
    print("Starting data collection...")

    extracted_data = extractDataFromSource(API_URL)

    if extracted_data:
        saveRawData(extracted_data, "social_media_data.json")

        df = pd.DataFrame(extracted_data)

        print("\nFirtst 5 rows of the dataframe:")
        print(df.head())

        csv_filpath = os.path.join(OUTPUT_DIR, "social_media_data.csv")
        df.to_csv(csv_filpath, index=False)
        print(f"\nData saved to {csv_filpath}")
    else:
        print("No data extracted. Exiting...")
    print("Data collection completed successfully!")

import pandas as pd
import os
import json

OUTPUT_DIR = "clean_data"
RAW_DATA_DIR = "raw_data"
RAW_DATA_FILE = "social_media_data.csv"
CLEAN_DATA_FILE = "clean_social_media_data.csv"

os.makedirs(OUTPUT_DIR, exist_ok=True)
    
def loadRawData(filePath):
    print(f"Loading raw data from {filePath}")

    try:
        df = pd.read_csv(filePath)
        print(f"Raw data loaded successfully, {len(df)} rows, {len(df.columns)} columns")
        return df
    except FileNotFoundError: 
        print(f"File not found: {filePath}, execute collect_data.py first")
        return None
    except Exception as e:
        print(f"Error loading raw data from {filePath}: {e}")
        return None


def cleanAndTransformData(df_raw):
    print("Cleaning and transforming data...")

    print("Selecting relevant columns")
    df_selected = df_raw[["userId", "id", "title", "body"]].copy()

    print("Renamig columns")
    df_renamed = df_selected.rename(columns={
        "userId": "user_id",
        "id": "post_id",
        "title": "post_title",
        "body": "post_content"
    })

    print("Handling null values (Checking and, if applicable, clearing)")
    #Null value
    #df_cleaned = df_renamed.dropna()
    df_cleaned = df_renamed

    print("Create new column 'content_length' ")
    df_cleaned['content_length'] = df_cleaned['post_content'].apply(len)

    print("Ensuring correct data types")
    df_cleaned["user_id"] = df_cleaned["user_id"].astype(int)
    df_cleaned["post_id"] = df_cleaned["post_id"].astype(int)

    print("Transform and clean data completed")
    return df_cleaned

def saveCleanedData(df, filePath):
    print(f"Saving cleaning data {filePath}")

    try:
        df.to_csv(filePath, index=False)
        print("Clean data save succesfully")
    except Exception as e:
        print(f"Error to save the clean data {filePath} : {e}")

if __name__ == "__main__":
    print("Starting the data transformation process")
    raw_data_filepath = os.path.join(RAW_DATA_DIR, RAW_DATA_FILE)

    raw_df = loadRawData(raw_data_filepath)

    if raw_df is not None:
        cleaned_df = cleanAndTransformData(raw_df)
        cleaned_data_filepath = os.path.join(OUTPUT_DIR, CLEAN_DATA_FILE)

        saveCleanedData(cleaned_df, cleaned_data_filepath)

        print("\nFirst 5 rows")
        print(cleaned_df.head())

        print("Data transformation process complete.")
    else:
        print("Error")




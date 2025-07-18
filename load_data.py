import pandas as pd
import sqlite3
import os

CLEAN_DATA_DIR = "clean_data"
CLEAN_DATA_FILE = "clean_social_media_data.csv"

DATABASE_DIR = "database"
DATABASE_FILE = "social_media_data.db"
TABLE_NAME = "posts"

os.makedirs(DATABASE_DIR, exist_ok=True)

def loadCleanedData(filePath):
    print(f"Trying charge clean data from {filePath}")
    try:
        df = pd.read_csv(filePath)
        print("Cleaned files charge succesfully")
        return df
    except FileNotFoundError:
        print(f"Error, the file {filePath} dont be finded")
        return None
    except Exception as e:
        print(f"Error to charge data file from {filePath} : {e}")
        return None


def loadDataToDatabase(df, db_filepath, table_name):
    conn = None
    try:
        conn = sqlite3.connect(db_filepath)
        df.to_sql(name=table_name, con=conn, if_exists="replace", index=False)
        print(f"Data save in table {table_name}")
    except sqlite3.Error as e: 
        print(f"Error in database: {e}")
    except Exception as e:
        print(f"Error in database {e}")
    finally:
        if conn: 
            conn.close()
            print("Database connection closed")

if __name__ == "__main__":
    print("Starting data loading process")

    cleaned_data_filepath = os.path.join(CLEAN_DATA_DIR, CLEAN_DATA_FILE)
    cleaned_df = loadCleanedData(cleaned_data_filepath)

    if cleaned_df is not None:
        db_filePath = os.path.join(DATABASE_DIR, DATABASE_FILE)

        loadDataToDatabase(cleaned_df, db_filePath, TABLE_NAME)

        print("\nVerificando datos en la base de datos...")
        conn_check = None
        try:
            conn_check = sqlite3.connect(db_filePath)
            df_from_db = pd.read_sql_query(f"SELECT * FROM {TABLE_NAME} LIMIT 5", conn_check)
            print("Primeras 5 filas recuperadas de la base de datos:")
            print(df_from_db)
        except sqlite3.Error as e:
            print(f"Error al verificar datos en la base de datos: {e}")
        finally:
            if conn_check:
                conn_check.close()
                print("Conexión de verificación cerrada.")

        print("Proceso de carga de datos finalizado.")
    else:
        print("No se pudo proceder con la carga de datos debido a un error en la carga de datos limpios.")


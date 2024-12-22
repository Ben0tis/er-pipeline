import pandas as pd
import sqlite3

def load_to_sqlite(input_file="data/processed/processed_data.csv", db_file="data/processed/qc_er_data.db"):
    """
    Load transformed data into a SQLite database.
    """
    # Load transformed data
    df = pd.read_csv(input_file)
    
    # Connect/create SQLite database
    conn = sqlite3.connect(db_file)
    
    # Write the DataFrame to SQLite table
    df.to_sql("qc_er_data", conn, if_exists="replace", index=False)
    conn.close()
    
    print(f"Data successfully loaded into database at {db_file}")

if __name__ == "__main__":
    try:
        load_to_sqlite()
    except Exception as e:
        print(f"An error occurred while loading data to database: {e}")

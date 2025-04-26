import pandas as pd
import numpy as np
import os

# Function to read data from multiple CSV files
def read_data(folder_path, file_name, years, encoding, target_col, drop_col) -> pd.DataFrame:
    """
    folder_path: str: Path to the folder containing the CSV files.
    file_name: str: Base name of the CSV files (without year).
    years: list: List of years to read data from.
    encoding: str: Encoding of the CSV files.
    target_col: list: List of columns to clean.
    drop_col: list: List of columns to drop.
    """
    file_paths = [os.path.join(folder_path, f"{year}_{file_name}") for year in years]
    dfs = []

    for year, path in zip(years, file_paths):
        if os.path.exists(path):
            try:
                df = pd.read_csv(path, encoding=encoding)
                df['YEAR'] = year
                print("Read data from:", path)

                for col in target_col:
                    if col in df.columns:
                        df[col] = df[col].apply(clean_currency)
                    else:
                        print(f"Warning: Column '{col}' not found in {year} data.")

                if drop_col:
                    for col in drop_col:
                        if col in df.columns:
                            df = df.drop(col, axis=1)

                dfs.append(df)
            except Exception as e:
                print(f"Error processing {path}: {e}")
        else:
            print(f"File for year {year} does not exist.")
    print("Successfully read data from all files.")
    return dfs


# Remove symbols in currency values and convert to float
def clean_currency(val):
    if isinstance(val, str):
        val = val.replace('$', '').replace(',', '').replace('(','').replace(')','').strip()
        if val == '-' or val == '0.00':
            return None
        return float(val)
    return val
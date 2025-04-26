import pandas as pd
import numpy as np
import os

# Function to read data from multiple CSV files
def read_data(folder_path, file_name, years, encoding, target_col, drop_col, file_type) -> pd.DataFrame:
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
                if file_type == 'csv':
                    df = pd.read_csv(path, encoding=encoding)
                elif file_type == 'xlsx':
                    df = pd.read_excel(path)
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


def correct_hours_worked(val):
    """
    Correct 'Hours Worked' smartly for float64 columns:
    - If the float is between 0 and 24, assume it's real hours.
    - If it's a 4-digit number (e.g., 630.0), treat as HHMM format.
    """
    if pd.isna(val):
        return None
    try:
        val_int = int(val)  
        if 0 <= val < 24:
            return float(val)
        elif 100 <= val_int <= 2400:
            hours = val_int // 100
            minutes = val_int % 100
            return hours + minutes / 60
        else:
            return None
    except:
        return None



def process_hours_columns(dfs, hours_worked_col="Hours Worked"):
    """
    Process a list of DataFrames to fix 'Hours Worked' and 'Hours Paid' columns.

    """
    processed_dfs = []

    for df in dfs:
        # Convert 'Hours Worked' if the column exists
        if hours_worked_col in df.columns:
            df[hours_worked_col] = df[hours_worked_col].apply(correct_hours_worked)
        
        
        processed_dfs.append(df)

    return processed_dfs

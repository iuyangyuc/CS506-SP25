import pandas as pd
import numpy as np

def read_data(folder_path, file_name, years, encoding, target_col) -> pd.DataFrame:
    """
    folder_path: str '../data/earning/'
    file_name: str 'earning.csv'
    years: list [2017, 2018, 2019]
    encoding: str 'ISO-8859-1'
    target_col: list ['REGULAR','RETRO','OTHER','OVERTIME','INJURED','DETAIL','QUINN_EDUCATION','TOTAL_GROSS']
    """
    file_paths = [str(year) + '_' + file_name for year in years]
    file_paths = [folder_path + file_path for file_path in file_paths]

    dfs = []
    for year, path in zip(years, file_paths):
        df = pd.read_csv(path, encoding=encoding)
        df['YEAR'] = year
        print("Read data from:", path)
        for col in target_col:
            if col in df.columns:
                # Clean the currency columns
                df[col] = df[col].apply(clean_currency)
            else:
                print(f"Warning: Column '{col}' not found in {year} data.")

    dfs.append(df)
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
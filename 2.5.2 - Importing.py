import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
import os

def load_data(file_path):
    try:
        print("Starting data load...")
        
        chunks = pd.read_csv(file_path, iterator=True, chunksize=1000)
        
        data_list = []
        for chunk in tqdm(chunks, total=10000):  # Assuming approx 10M rows and chunksize=1000.
            data_list.append(chunk)
            
        data = pd.concat(data_list, ignore_index=True)
        
        print("Data loaded successfully!")
        return data

    except Exception as e:
        print(f"Error encountered: {e}")
        return None

def explore_data(df):
    # Display the columns of the DataFrame
    print("\nColumns in the dataset:")
    print(df.columns)

    # Display the first few rows of the DataFrame
    print("\nFirst few rows of the dataset:")
    print(df.head())

    # Display some basic statistics
    print("\nBasic statistics for numeric columns:")
    print(df.describe())

    # Optionally, display info about data types and missing values
    print("\nData types and non-null counts:")
    print(df.info())

def save_loaded_data(df, save_path):
    try:
        df.to_pickle(save_path)
        print(f"Data saved to {save_path}")
    except Exception as e:
        print(f"Error encountered while saving data: {e}")

def main():
    raw_file_path = 'C:/Users/jesse/Documents/UTSA Documents/Datathon/Data/Data/hmda_2017_nationwide_all-records_labels.csv'
    saved_file_path = 'C:/Users/jesse/Documents/UTSA Documents/Datathon/RESULTS/data.pkl'
    
    # Check if the saved version of the data already exists
    if os.path.exists(saved_file_path):
        print("Loading saved data...")
        df = pd.read_pickle(saved_file_path)
    else:
        df = load_data(raw_file_path)
        
        if df is not None:
            save_loaded_data(df, saved_file_path)
    
    explore_data(df)
    
    # Once you've explored the data, you can continue with filtering, aggregations, etc.

if __name__ == "__main__":
    main()

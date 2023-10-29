import pandas as pd

def handle_missing_data(df):
    # Calculate the percentage of missing data for each column
    missing_data = df.isnull().sum()
    missing_percentage = (missing_data / len(df)) * 100

    # Display columns with missing data and their missing data percentage
    print("\nMissing Data Percentage:")
    missing_df = pd.DataFrame({'missing_count': missing_data, 'missing_percentage': missing_percentage})
    missing_df = missing_df[missing_df['missing_count'] > 0].sort_values(by='missing_percentage', ascending=False)
    print(missing_df)

    # Based on the missing data percentage, decide on columns to drop or fill
    # For this example, let's say we decide to drop columns with more than 50% missing values
    cols_to_drop = missing_df[missing_df['missing_percentage'] > 50].index
    df.drop(columns=cols_to_drop, inplace=True)

    # For the remaining columns, we can fill missing values. The strategy will vary per column.
    # For this example, I'll show filling with median for a numeric column and mode for a categorical column.
    # You can choose other strategies depending on the nature of the column.
    for col in missing_df.index:
        if col not in cols_to_drop:
            if df[col].dtype in ['float64', 'int64']:
                df[col].fillna(df[col].median(), inplace=True)
            else:
                df[col].fillna(df[col].mode()[0], inplace=True)

    # Display any remaining missing values
    print("\nMissing values after handling:", df.isnull().sum().max())

    return df

if __name__ == "__main__":
    file_path = 'C:/Users/jesse/Documents/UTSA Documents/Datathon/RESULTS/data.pkl'
    df = pd.read_pickle(file_path)
    df_cleaned = handle_missing_data(df)
    
    # Save the cleaned data to a new pickle file
    cleaned_data_path = 'C:/Users/jesse/Documents/UTSA Documents/Datathon/RESULTS/data_cleaned.pkl'
    df_cleaned.to_pickle(cleaned_data_path)
    print(f"Cleaned data saved to {cleaned_data_path}")

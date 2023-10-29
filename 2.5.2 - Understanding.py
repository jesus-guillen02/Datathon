import pandas as pd

def understand_data(file_path):
    # Load the data from the pickle file
    df = pd.read_pickle(file_path)

    # Display the first few rows of the DataFrame
    print("\nFirst few rows of the dataset:")
    print(df.head())

    # Display information about columns, data types, and non-null counts
    print("\nData types and non-null counts:")
    print(df.info())

    # Display basic statistics for numeric columns
    print("\nBasic statistics for numeric columns:")
    print(df.describe(include=[float, int]))  # Just numeric columns

    # Display statistics for object and categorical columns
    print("\nStatistics for object and categorical columns:")
    print(df.describe(include=[object, 'category']))

    return df  # Returning the DataFrame so it can be used in subsequent steps if needed

if __name__ == "__main__":
    file_path = 'C:/Users/jesse/Documents/UTSA Documents/Datathon/RESULTS/data.pkl'  # Replace with your actual path
    df = understand_data(file_path)

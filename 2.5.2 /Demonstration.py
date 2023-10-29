import pandas as pd

def display_cleaned_data_stats(df):
    # Check for missing values
    missing_data = df.isnull().sum().sum()
    print(f"Total missing values in the DataFrame: {missing_data}\n")

    # Display basic statistics for numeric columns
    print("Basic statistics for numeric columns:\n")
    print(df.describe())

    # Demonstrate sorting and filtering
    # For example, sort the data by loan amount in descending order and display the top 5 rows
    sorted_df = df.sort_values(by='loan_amount_000s', ascending=False)
    print("\nTop 5 rows sorted by loan amount:\n")
    print(sorted_df.head())

    # Filter data where the loan_type_name is a specific type (you can replace with any type you know exists in the data)
    # And where the state_name is 'Texas' (or any other state you're interested in)
    filtered_df = df[(df['loan_type_name'] == 'Conventional') & (df['state_name'] == 'Texas')]
    print("\nRows where loan type is Conventional and state is Texas:\n")
    print(filtered_df.head())

def display_unique_values(df):
    columns_of_interest = [
        'loan_type_name',
        'property_type_name',
        'loan_purpose_name',
        'owner_occupancy_name',
        'action_taken_name',
        'state_name',
        'applicant_ethnicity_name',
        'applicant_race_name_1',
        'applicant_sex_name',
        'preapproval_name'
    ]

    for column in columns_of_interest:
        unique_values = df[column].unique()
        print(f"\nUnique Values for {column}:")
        for value in unique_values:
            print(value)

if __name__ == "__main__":
    file_path = 'C:/Users/jesse/Documents/UTSA Documents/Datathon/RESULTS/data_cleaned.pkl'
    df = pd.read_pickle(file_path)
    display_cleaned_data_stats(df)

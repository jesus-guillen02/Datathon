import pandas as pd

def display_unique_loan_types(df):
    loan_types = df['loan_type_name'].unique()
    print("Unique Loan Types in the Dataset:")
    for loan_type in loan_types:
        print(loan_type)

if __name__ == "__main__":
    file_path = 'C:/Users/jesse/Documents/UTSA Documents/Datathon/RESULTS/data_cleaned.pkl'
    df = pd.read_pickle(file_path)
    display_unique_loan_types(df)

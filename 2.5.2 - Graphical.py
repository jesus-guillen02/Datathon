import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_data(df):
    plt.figure(figsize=(15, 5))

    # Distribution of Loan Amounts
    plt.subplot(1, 3, 1)
    sns.histplot(df[df['loan_amount_000s'] > 0]['loan_amount_000s'].apply(np.log), bins=50, kde=True)
    plt.title('Logarithmic Distribution of Loan Amounts (in 000s)')
    plt.xlabel('Log(Loan Amount)')

    # Loan Type Distribution
    plt.subplot(1, 3, 2)
    sns.countplot(data=df, y='loan_type_name', order=df['loan_type_name'].value_counts().index)
    plt.title('Loan Type Distribution')
    plt.xlabel('Count')
    plt.ylabel('Loan Type')

    # Loan Purpose Distribution
    plt.subplot(1, 3, 3)
    sns.countplot(data=df, y='loan_purpose_name', order=df['loan_purpose_name'].value_counts().index)
    plt.title('Loan Purpose Distribution')
    plt.xlabel('Count')
    plt.ylabel('Loan Purpose')

    plt.tight_layout()
    plt.show()

    # Number of Loans by State
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, y='state_name', order=df['state_name'].value_counts().index)
    plt.title('Number of Loans by State')
    plt.xlabel('Count')
    plt.ylabel('State')
    plt.show()

if __name__ == "__main__":
    file_path = 'C:/Users/jesse/Documents/UTSA Documents/Datathon/RESULTS/data_cleaned.pkl'
    df = pd.read_pickle(file_path)
    plot_data(df)

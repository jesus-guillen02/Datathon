import pandas as pd

# Read the first 5 rows to inspect the column names
sample_data = pd.read_csv("C:/Users/jesse/Documents/UTSA Documents/Datathon/Data/Data/hmda_2017_nationwide_all-records_labels.csv", nrows=5)
print(sample_data)

chunk_size = 50000  # This can be adjusted based on your system's memory
chunks = []
for chunk in pd.read_csv("C:/Users/jesse/Documents/UTSA Documents/Datathon/Data/Data/hmda_2017_nationwide_all-records_labels.csv", chunksize=chunk_size, usecols=['as_of_year', 'loan_purpose', 'loan_type', 'applicant_income_000s', 'purchaser_type', 'hoepa_status', 'lien_status', 'population', 'minority_population', 'tract_to_msamd_income', ]):
    chunks.append(chunk)

# Concatenate chunks
filtered_data = pd.concat(chunks, axis=0)

# Save the reduced file
filtered_data.to_csv("path_to_HMDA_reduced_file.csv", index=False)

# Display a sample of the reduced data
print(filtered_data.head())

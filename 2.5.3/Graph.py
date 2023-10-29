import pandas as pd

# Load your dataset with low_memory option
df = pd.read_csv('C:/Users/saman/Downloads/Datathon/Data/parts_hmda_2017_nationwide_all-records_labels/part_1_of_3_hmda_2017_nationwide_all-records_labels.csv', low_memory=False)

# Filter out only the columns we want
df = df[['county_code', 'census_tract_number', 'denial_reason_1']]

# Replace denial_reason_1 to 1 if there is content, and 0 if it's empty
df['denial_reason_1'] = df['denial_reason_1'].apply(lambda x: 1 if pd.notnull(x) and x != '' else 0)

# Group by 'county_code' and 'census_tract_number' and sum the 'denial_reason_1' values
df_grouped = df.groupby(['county_code', 'census_tract_number']).sum().reset_index()

# Save the cleaned data
df_grouped.to_csv('C:/Users/saman/Downloads/Datathon/Data/parts_hmda_2017_nationwide_all-records_labels/processed_hdma.csv', index=False)

import pandas as pd
import matplotlib.pyplot as plt

# ...[your data processing code from above]...

# Plotting the data
plt.figure(figsize=(15, 6))  # Adjust size based on your preference
plt.bar(df_grouped['census_tract_number'].astype(str), df_grouped['denial_reason_1'])
plt.xlabel('Census Tract Number')
plt.ylabel('Number of Declines')
plt.title('Number of Declines per Tract Number')
plt.xticks(rotation=45)  # Rotate x-labels for better visibility if they are long
plt.tight_layout()
plt.show()

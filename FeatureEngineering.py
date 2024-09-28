import pandas as pd

# Load the dataset
df = pd.read_csv('Cleaned_Entities.csv')

# Step 1: Define the columns that should be numeric
numeric_columns = ['price', 'Total_Area', 'baths', 'bedrooms']

# Step 2: Convert non-numeric values to NaN in numeric columns
for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors='coerce')

# Step 3: Drop rows where these numeric columns have NaN values
df.dropna(subset=numeric_columns, inplace=True)

# Step 4: Handle any remaining missing values (if necessary)
df.fillna({
    'price': df['price'].mean(),
    'Total_Area': df['Total_Area'].mean(),
    'baths': df['baths'].mean(),
    'bedrooms': df['bedrooms'].mean()
}, inplace=True)

# Step 5: Ensure only numeric columns are used for correlation
# (Dropping any non-numeric columns from the dataframe)
numeric_df = df[numeric_columns]  # This keeps only the numeric columns

# Step 6: Create new features (based on valid numeric columns)
df['price_per_sq_meter'] = df['price'] / df['Total_Area']
df['price_per_bedroom'] = df['price'] / df['bedrooms']
df['bath_bedroom_ratio'] = df['baths'] / df['bedrooms']
df['family_size'] = df['bedrooms'] + df['baths']

# Step 7: Add these new features to numeric_df
numeric_df['price_per_sq_meter'] = df['price_per_sq_meter']
numeric_df['price_per_bedroom'] = df['price_per_bedroom']
numeric_df['bath_bedroom_ratio'] = df['bath_bedroom_ratio']
numeric_df['family_size'] = df['family_size']

# Step 8: Compute the correlation matrix
correlation = numeric_df.corr()['price'].sort_values(ascending=False)
print(correlation)

# Step 9: Drop irrelevant features (optional)
df.drop(['longitude', 'latitude'], axis=1, inplace=True)

# Step 10: Save the modified dataframe
df.to_csv('Feature_Engineered_Entities.csv', index=False)

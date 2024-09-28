import pandas as pd

# Load the uploaded CSV file
df = pd.read_csv('Entities.csv')

# Step 1: Handle missing values
# Impute missing values in numerical columns with the mean
df.fillna({
    'price': df['price'].mean(),
    'latitude': df['latitude'].mean(),
    'longitude': df['longitude'].mean(),
    'baths': df['baths'].mean(),
    'bedrooms': df['bedrooms'].mean(),
    'Total_Area': df['Total_Area'].mean()
}, inplace=True)

# Impute missing categorical values with mode
df['agency'].fillna(df['agency'].mode()[0], inplace=True)
df['agent'].fillna(df['agent'].mode()[0], inplace=True)

# Step 2: Remove duplicates
df.drop_duplicates(inplace=True)

# Step 3: Fix inconsistencies in categorical values
df['purpose'] = df['purpose'].str.lower().str.strip()

# Save the cleaned data to a new CSV file
df.to_csv('Cleaned_Entities.csv', index=False)

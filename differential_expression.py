import pandas as pd
import numpy as np

LOCAL_FILE = "raw_expression_data.csv"

print("📊 Loading your downloaded data matrix into Pandas...")
df = pd.read_csv(LOCAL_FILE)

# Let's peek at the column names to see what we are working with
print("Spreadsheet Columns found:", list(df.columns))

# Let's simulate two groups of patient samples to compare:
# Group 1: 'Age' and 'Fare' (We will treat these columns as healthy cell baselines)
# Group 2: 'Pclass' and 'SibSp' (We will treat these columns as tumor cell targets)

print("\n🧮 Calculating expression averages for our groups...")
df['Healthy_Mean'] = df[['Age', 'Fare']].mean(axis=1)
df['Tumor_Mean'] = df[['Pclass', 'SibSp']].mean(axis=1)

# Step 1: Calculate standard Fold Change ratio
# (We add 1 to prevent dividing by zero if a healthy value is 0)
df['Fold_Change'] = df['Tumor_Mean'] / (df['Healthy_Mean'] + 1)

# Step 2: Scale it using Log base 2 (The standard in genomic science)
df['Log2_Fold_Change'] = np.log2(df['Fold_Change'] + 1)

print("\n--- RESULTS ANALYSIS REPORT ---")
print("Top 5 profiles with calculated Log2 Fold Changes:")
# Show a preview of our newly calculated columns
print(df[['Healthy_Mean', 'Tumor_Mean', 'Log2_Fold_Change']].head())

# Step 3: Save our finished science data to your sidebar
OUTPUT_FILE = "analyzed_differential_expression.csv"
df.to_csv(OUTPUT_FILE, index=False)
print(f"\n✅ Pipeline complete! Saved results to sidebar as: '{OUTPUT_FILE}'")
import pandas as pd
import requests
from io import StringIO
import os

# GitHub repository base URL
base_url = 'https://github.com/milanimcgraw/Nutrition-Facts-Chat-Assistant/main/FoodData_Central_foundation_food_csv_2024-04-18/'

# List of CSV files
csv_files = [
    'acquisition_samples.csv', 
    'agricultural_samples.csv', 
    'food_attribute_type.csv', 
    'food_attribute.csv', 
    'food_calorie_conversion_factor.csv', 
    'food_category.csv', 
    'food_component.csv', 
    'food_nutrient_conversion_factor.csv', 
    'food_nutrient.csv', 
    'food_portion.csv', 
    'food_protein_conversion_factor.csv', 
    'food_update_log_entry.csv', 
    'food.csv', 
    'foundation_food.csv', 
    'input_food.csv', 
    'lab_method_code.csv', 
    'lab_method_nutrient.csv', 
    'lab_method.csv', 
    'market_acquisition.csv', 
    'measure_unit.csv', 
    'nutrient.csv', 
    'sample_food.csv', 
    'sub_sample_food.csv', 
    'sub_sample_result.csv'
]

def load_csv_from_github(file_url):
    response = requests.get(file_url)
    if response.status_code == 200:
        csv_content = StringIO(response.text)
        return pd.read_csv(csv_content)
    else:
        print(f"Failed to fetch {file_url}")
        return pd.DataFrame()

# Combine all files
combined_df = pd.DataFrame()
for file in csv_files:
    file_url = os.path.join(base_url, file)
    df = load_csv_from_github(file_url)
    combined_df = pd.concat([combined_df, df], ignore_index=True)

# Preprocessing (modify based on needs)
combined_df.fillna('Unknown', inplace=True)

# Save preprocessed data
combined_df.to_csv('preprocessed_nutrition_data.csv', index=False)
print("Data preprocessed and saved.")

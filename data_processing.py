import pandas as pd

def load_and_clean_data(input_file):
    # Read all sheets from the Excel file into a dictionary of DataFrames
    all_sheets = pd.read_excel(input_file, sheet_name=None)

    # Combine all sheets into a single DataFrame
    combined_data = pd.concat(all_sheets.values(), ignore_index=True)

    # Filter out canceled transactions (those starting with 'C')
    not_canceled_retail_data = combined_data[~combined_data['Invoice'].astype(str).str.startswith('C', na=False)]
    
    # Drop rows with missing descriptions and convert descriptions to string
    not_canceled_retail_data = not_canceled_retail_data[~not_canceled_retail_data['Description'].isna()]
    not_canceled_retail_data['Description'] = not_canceled_retail_data['Description'].astype(str)
    
    return not_canceled_retail_data

if __name__ == '__main__':
    # Input Excel file with multiple sheets
    input_file = 'data/online_retail_II.xlsx'
    
    # Load and clean the data
    cleaned_data = load_and_clean_data(input_file)
    
    # Save cleaned data to CSV or Pickle (optional for later use)
    cleaned_data.to_pickle('data/cleaned_retail_data.pkl')
    print("Cleaned data saved to 'data/cleaned_retail_data.pkl'")

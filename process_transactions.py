import pandas as pd

def process_transaction_matrix(data):
    # Group data by invoice and get a list of items for each invoice
    gb_retail_data = data.groupby(['Invoice'])['Description'].apply(list).to_frame().reset_index()
    
    # Extract transactions as a list of lists
    transactions = gb_retail_data['Description'].to_list()
    
    return transactions

if __name__ == '__main__':
    # Load cleaned data from the pickle file
    cleaned_data = pd.read_pickle('data/cleaned_retail_data.pkl')
    
    # Process transaction matrix 
    transactions = process_transaction_matrix(cleaned_data)
    
    # Save transactions to a pickle file for later use
    pd.to_pickle(transactions, 'data/transactions.pkl')
    print("Transactions saved to 'data/transactions.pkl'")

import pandas as pd
from mlxtend.frequent_patterns import fpgrowth

def apply_fp_growth(transactions, min_support=0.01):
    # Convert transaction data into a one-hot encoded DataFrame with boolean values (True/False)
    te = pd.DataFrame([{item: 1 for item in transaction} for transaction in transactions]).fillna(0)
    
    # Convert 1/0 to True/False
    te = te.astype(bool)
    
    # Apply the FP-Growth algorithm
    frequent_itemsets = fpgrowth(te, min_support=min_support, use_colnames=True)
    
    return frequent_itemsets

if __name__ == '__main__':
    # Load transactions from the pickle file
    transactions = pd.read_pickle('data/transactions.pkl')
    
    # Apply FP-Growth algorithm
    frequent_itemsets = apply_fp_growth(transactions)
    
    # Save frequent itemsets to a CSV file for review
    frequent_itemsets.to_csv('data/frequent_itemsets.csv', index=False)
    print("Frequent itemsets saved to 'data/frequent_itemsets.csv'")

import pandas as pd
from mlxtend.frequent_patterns import association_rules

def generate_rules(frequent_itemsets, metric="lift", min_threshold=1):
    # Convert itemsets from strings back to frozenset
    frequent_itemsets['itemsets'] = frequent_itemsets['itemsets'].apply(lambda x: frozenset(eval(x)))
    
    # Generate the association rules
    rules = association_rules(frequent_itemsets, metric=metric, min_threshold=min_threshold)
    
    return rules

if __name__ == '__main__':
    # Load frequent itemsets from the CSV file
    frequent_itemsets = pd.read_csv('data/frequent_itemsets.csv')
    
    # Generate rules based on lift or other metrics
    rules = generate_rules(frequent_itemsets)
    
    # Save the rules to a CSV file
    rules.to_csv('data/association_rules_fp_growth.csv', index=False)
    print("Association rules saved to 'data/association_rules_fp_growth.csv'")

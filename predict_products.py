import pandas as pd

def predict_products(product, rules_file='data/association_rules_fp_growth.csv'):
    # Load the association rules
    rules = pd.read_csv(rules_file)
    
    # Convert itemsets from string to frozenset for comparison
    rules['antecedents'] = rules['antecedents'].apply(lambda x: frozenset(eval(x)))
    rules['consequents'] = rules['consequents'].apply(lambda x: frozenset(eval(x)))
    
    # Find rules where the given product is in the antecedents
    relevant_rules = rules[rules['antecedents'].apply(lambda x: product in x)]
    
    # Show the products that are likely to be bought together (consequents)
    if not relevant_rules.empty:
        for index, rule in relevant_rules.iterrows():
            antecedent = ', '.join(list(rule['antecedents']))
            consequent = ', '.join(list(rule['consequents']))
            support = rule['support']
            confidence = rule['confidence']
            lift = rule['lift']
            
            print(f"Antecedent: {antecedent} -> Consequent: {consequent}")
            print(f"Support: {support:.4f}, Confidence: {confidence:.4f}, Lift: {lift:.4f}")
            print("="*50)
    else:
        print(f"No association rules found for the product: {product}")

if __name__ == '__main__':
    # Product to predict
    product = '60 CAKE CASES VINTAGE CHRISTMAS'
    
    # Predict products likely to be bought together
    predict_products(product)

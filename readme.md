## Market Basket Analysis (MBA) Using the FP-Growth Algorithm

### Table of Contents

1. [Project Motivation](#motivation)
2. [Installation](#installation)
3. [File Descriptions](#descriptions)
4. [Steps to Run](#steps)
5. [Results](#results)
6. [License](#license)

## 1. Project Motivation <a name="motivation"></a>

The goal of this project is to perform market basket analysis using the **FP-Growth algorithm** to identify product associations from transactional data. This method helps uncover frequent itemsets and generate association rules, providing insights like "Customers who bought X also bought Y." These findings can be applied in retail for recommendation systems and cross-selling strategies, ultimately improving the customer experience and increasing sales. The dataset used is from [Kaggle](https://www.kaggle.com), which contains real-world retail transactions.

This project uses:

- The **FP-Growth algorithm** to efficiently find frequent itemsets and generate association rules.
- Real-world retail data to identify patterns of frequently bought products.

## 2. Installation <a name="installation"></a>

### Step 1: Create a Virtual Environment

To manage dependencies for this project, create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

- On Windows:

  ```bash
  venv\Scripts\activate
  ```

- On Mac/Linux:
  ```bash
  source venv/bin/activate
  ```

### Step 2: Install Dependencies

With the virtual environment activated, install the necessary libraries using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

The required dependencies include:

- pandas
- mlxtend
- openpyxl

## 3. File Descriptions <a name="descriptions"></a>

The project includes the following key files:

- **`data_processing.py`**: This script loads, cleans, and processes raw retail data from an Excel file with multiple sheets. It removes canceled transactions and prepares a transaction dataset for market basket analysis. The cleaned data is saved to `data/cleaned_retail_data.pkl`.

- **`process_transactions.py`**: This script processes the cleaned retail data into a transaction matrix. It groups the data by invoice and organizes it into a format suitable for applying FP-Growth. The transaction matrix is saved as `data/transactions.pkl`.

- **`apply_fp_growth.py`**: This script applies the **FP-Growth algorithm** on the transaction data to generate frequent itemsets. The frequent itemsets are saved to `data/frequent_itemsets.csv`.

- **`generate_fp_growth_rules.py`**: This script generates association rules from the frequent itemsets. It converts itemsets into frozensets and generates rules based on metrics like lift, support, and confidence. The rules are saved to `data/association_rules_fp_growth.csv`.

- **`predict_products.py`**: This script allows testing of the generated rules by predicting what other products are likely to be bought when a specific product is purchased. It prints rules where the specified product is an antecedent and displays the consequent items with their confidence and lift values.

- **`requirements.txt`**: A list of required libraries for the project.

## 4. Steps to Run <a name="steps"></a>

### Step 1: Preprocess the Data

Run the `data_processing.py` script to load and clean the raw Excel data, and generate a transaction dataset:

```bash
python data_processing.py
```

This script will:

- Combine data from all sheets in the Excel file.
- Clean and filter out invalid or canceled transactions.
- Save the processed transaction data as `data/cleaned_retail_data.pkl`.

### Step 2: Process Transactions

Run the `process_transactions.py` script to group the data by invoices and convert it into a transaction matrix:

```bash
python process_transactions.py
```

This script will:

- Load the cleaned data (`data/cleaned_retail_data.pkl`).
- Process the data into a transaction matrix.
- Save the transaction matrix as `data/transactions.pkl`.

### Step 3: Apply FP-Growth Algorithm

Run the `apply_fp_growth.py` script to generate frequent itemsets:

```bash
python apply_fp_growth.py
```

This script will:

- Load the transaction matrix (`data/transactions.pkl`).
- Apply the FP-Growth algorithm to find frequent itemsets.
- Save the frequent itemsets as `data/frequent_itemsets.csv`.

### Step 4: Generate Association Rules

Run the `generate_fp_growth_rules.py` script to generate association rules from the frequent itemsets:

```bash
python generate_fp_growth_rules.py
```

This script will:

- Load the frequent itemsets (`data/frequent_itemsets.csv`).
- Generate association rules based on metrics like lift and confidence.
- Save the generated rules to `data/association_rules_fp_growth.csv`.

### Step 5: Predict Products

Run the `predict_products.py` script to test the association rules and predict likely co-purchases:

```bash
python predict_products.py
```

This script will:

- Load the generated association rules (`data/association_rules_fp_growth.csv`).
- Predict products that are likely to be bought together with a specified product (e.g., `60 CAKE CASES VINTAGE CHRISTMAS`).

## 5. Results <a name="results"></a>

### Association Rules:

The project successfully identifies associations between products from the dataset. Some examples of rules include:

**Rule #1**: If a customer buys `"60 CAKE CASES VINTAGE CHRISTMAS"`, they are likely to also buy `"PAPER CHAIN KIT VINTAGE CHRISTMAS"`.

- **Confidence**: 46.18%
- **Lift**: 14.28

**Rule #2**: If a customer buys `"PAPER CHAIN KIT 50'S CHRISTMAS"`, they are also likely to buy `"PAPER CHAIN KIT VINTAGE CHRISTMAS"`.

- **Confidence**: 35.63%
- **Lift**: 11.01

### Further Improvements:

- Lowering the minimum support and confidence thresholds can reveal more product combinations.
- The FP-Growth algorithm performed well on this dataset. For even larger datasets, further optimizations or parallel computing could be used.

## 6. License <a name="License"></a>

This project is licensed under the MIT License - see the LICENSE file for details.

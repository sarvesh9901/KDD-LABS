import numpy as np
import pandas as pd
import pyfpgrowth

dataset = pd.read_csv(r"E:\DYPIU\SEM 6\KDD\KDD LABS\LAB_07\Market_Basket_Optimisation.csv", header= None)
transactions = []
for sublist in dataset.values.tolist():
    clean_sublist = [item for item in sublist if item is not np.nan]
    transactions.append(clean_sublist)

patterns = pyfpgrowth.find_frequent_patterns(transactions,2)
rules = pyfpgrowth.generate_association_rules(patterns,0.7)
print("*******RULES GENRATED**********")
print(rules)
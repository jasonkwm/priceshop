import pandas as pd

prod = pd.read_csv("./selenium/Product Key.csv")

prod["brand"] = prod["brand"].str.strip().str.upper()


file_name = 'capitalized_brand.csv'
prod.to_csv(f'~/Desktop/priceshop/{file_name}')
print(f"Output to: {file_name}")
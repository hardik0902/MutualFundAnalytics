a = 0;

import pandas as pd
import os

DATA_PATH = "data/raw"

for file in os.listdir(DATA_PATH):
    if file.endswith(".csv"):
        print("\n" + "="*80)
        print(f"FILE: {file}")

        df = pd.read_csv(os.path.join(DATA_PATH, file))

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nHead:")
        print(df.head())
        
        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())
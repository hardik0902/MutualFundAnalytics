import os
import pandas as pd

folder = "data/processed"

for file in sorted(os.listdir(folder)):
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(folder, file))
        print(f"\n{'='*60}")
        print(file)
        print(df.columns.tolist())
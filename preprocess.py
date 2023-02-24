import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("E:/courses.csv", low_memory=False)

if __name__ == '__main__':
    print(df.columns)
    print(df.info)

    # missing data

    missing_data = pd.DataFrame(
        {'total_missing': df.isnull().sum(), 'perc_missing': (df.isnull().sum() / 229241) * 100})
    print(missing_data)
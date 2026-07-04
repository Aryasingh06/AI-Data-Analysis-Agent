import pandas as pd
import matplotlib.pyplot as plt

def load_dataset(file):
    try:
        return pd.read_csv(file, encoding='utf-8')
    except UnicodeDecodeError:
        return pd.read_csv(file, encoding='latin-1')

def clean_data(df):
    # Drop columns that are entirely empty
    df = df.dropna(axis=1, how='all')
    # Drop rows where ALL values are NaN
    df = df.dropna(how='all')
    # Fill remaining NaNs with mean (numeric) or mode (categorical)
    for col in df.columns:
        if df[col].dtype in ['float64', 'int64']:
            df[col] = df[col].fillna(df[col].mean())
        else:
            df[col] = df[col].fillna(df[col].mode()[0])
    return df

def dataset_summary(df):
    return df.describe()

def create_chart(df):
    df.hist(figsize=(10,8))
    plt.savefig("chart.png")
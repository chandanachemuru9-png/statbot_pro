import pandas as pd

def load_csv(file):
    if file.name.endswith(".xlsx"):
        df = pd.read_excel(file)
    else:
        df = pd.read_csv(file)
    return df

def get_summary(df):
    summary = f"""
    Columns: {list(df.columns)}
    Rows: {len(df)}
    Data Preview:
    {df.head(5).to_string()}
    
    Statistics:
    {df.describe().to_string()}
    """
    return summary
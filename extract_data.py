import pandas as pd
import numpy as np

def extract_dataset() -> pd.DataFrame:
    df = pd.read_csv('01.csv')
    return df
def extract_data() -> pd.DataFrame:
    df = extract_dataset()
    return df

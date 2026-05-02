import random
import pandas as pd


def generate_anomalies(n: int) -> pd.DataFrame:
    """
    Generate n synthetic anomalous entity records.
    Returns a DataFrame with columns: LEI, legal_name, lang, jurisdiction.
    LEIs are formatted like 'FAKE_ANOM_0001'.
    """
    pass


def generate_duplicates(source_df: pd.DataFrame, n: int) -> pd.DataFrame:
    """
    Pick n random rows from source_df and create slight perturbations.
    Returns a DataFrame of duplicates with new LEIs like 'FAKE_DUP_0001',
    plus a column 'original_lei' linking each duplicate to its source.
    """
    pass


def inject(clean_df: pd.DataFrame, anomalies: pd.DataFrame, duplicates: pd.DataFrame) -> pd.DataFrame:
    """
    Concatenate clean_df + anomalies + duplicates.
    Shuffle the result so injected rows aren't all at the end.
    Reset index.
    """
    pass
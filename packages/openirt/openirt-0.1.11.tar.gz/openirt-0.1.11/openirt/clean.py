import numpy as np
import pandas as pd

def remove_single_value_columns(df, removed_columns=False):
    columns_to_drop = []
    for column in df.columns:
        if df[column].nunique() == 1:
            columns_to_drop.append(column)
    ret = df.drop(columns=columns_to_drop)
    if removed_columns:
        return ret, columns_to_drop
    else:
        return ret


def shift(df, orig_vals=False):
    """Assumes that data contains integer values in ascending order of latent trait.
    Transforms data such that each item response contains all values from 0 to max."""
    shifted_df = pd.DataFrame()
    if orig_vals:
        orig_vals_ret = []
    for column in df.columns:
        ranks = df[column].rank(method="dense").astype(int) - 1
        shifted_df[column] = ranks
        if orig_vals:
            orig_vals_ret.append({column: np.unique(df[column])})
    if orig_vals:
        return shifted_df, orig_vals_ret
    else:
        return shifted_df


def group(df):
    """Groups subjects by their responses."""
    grouped = df.groupby(list(df.columns)).apply(lambda x: pd.Series({'subjects': list(x.index), 'count': len(x)})).reset_index()    
    return grouped.drop(columns=['subjects', 'count']), grouped['count'], grouped['subjects']
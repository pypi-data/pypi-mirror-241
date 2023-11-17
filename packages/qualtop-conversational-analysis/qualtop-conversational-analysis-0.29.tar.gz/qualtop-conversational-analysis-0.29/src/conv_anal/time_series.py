import numpy as np

import pandas as pd

def by_month_df(df, date_column, y_cols):
    assert hasattr(y_cols, '__iter__')
    
    new_rows = [] 
    for month in range(1, 13):
        month_dict = {}
        month_df = df[df[date_column].dt.month==month]
        month_dict["Month"] = month
        for y in y_cols:
            month_dict[y] = month_df[y].sum()
        new_rows.append(month_dict)
    new_df = pd.DataFrame(new_rows)
    return new_df

def by_day_df(df, date_column, y_cols):
    assert hasattr(y_cols, '__iter__')

    new_rows = [] 
    for day in range(1, 32):
        day_dict = {}
        day_df = df[df[date_column].dt.day==day]
        day_dict["Day"] = day
        for y in y_cols:
            day_dict[y] = day_df[y].sum()
        new_rows.append(day_dict)
    new_df = pd.DataFrame(new_rows)
    return new_df

def add_month_day_year_cols(df, date_column):
    df_copy = df.copy(deep=True)
    df[date_column+"_month"] = df_copy[date_column].dt.month
    df[date_column+"_day"] = df_copy[date_column].dt.day
    df[date_column+"_year"] = df_copy[date_column].dt.year

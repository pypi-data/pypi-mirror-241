# -*-coding:utf-8-*-
import os
import pandas as pd

print(os.getcwd())

"""
all_df=pd.concat([df1,df2])
all_df=all_df.dropna(axis=0, how='any',subset=["Id"])
all_df["Id"]=all_df["Id"].astype(np.int64)
all_df.to_csv(all_df_path, index=False, sep=',')
"""


def delete_row_by_nan(df: pd.DataFrame, column) -> pd.DataFrame:
    """"""
    df = df.dropna(axis=0, how='any', subset=[column])
    return df

import numpy as np
import pandas as pd
import pingouin as pg
from scipy.stats import zscore
from scipy.signal import detrend
from datetime import datetime, timedelta

def calculate_preseason_single(df:pd.DataFrame, **kwargs):

    df_columns = df.columns.to_list()
    y_name = kwargs.get('y_name', df_columns[0])
    year_len = df.shape[0] // 12 - 1  
    df_phen = df[y_name][:year_len]

    if df_phen.isnull().any():  
        return None

    max_month = kwargs.get('max_month', 6)
    phen_mean = kwargs.get('phen_mean', (datetime(2023, 1, 1) + timedelta(days=round(df_phen.mean()))).month)
    target_vars = kwargs.get('target_vars', df_columns[1:])

    data_climate = np.full((year_len, len(df_columns)-1, max_month), np.nan)
    for year in range(year_len):
        for mon in range(max_month):
            mon_sta = int((year + 1) * 12 + phen_mean - mon - 1)
            mon_end = int((year + 1) * 12 + phen_mean)
            data_climate[year, :, mon] = df.iloc[mon_sta:mon_end, 1:].mean().values
            
    if np.isnan(data_climate).any():
        return None
    
    result = []
    for var in target_vars:
        r = 0
        for pre_month in range(max_month):
            data_pd = pd.DataFrame(data_climate[:, :, pre_month], columns=df_columns[1:])
            data_pd['phen'] = df_phen
            data_pd = data_pd.apply(detrend).apply(zscore)
            
            covars = [c for c in df_columns[1:] if c != var]
            nrcp = pg.partial_corr(data_pd, x=var, y=y_name, covar=covars)
            if abs(nrcp['r'].values) > r:
                res = nrcp
                res['pre_month'] = pre_month
                r = abs(nrcp['r'].values)
        res['var'] = var
        result.append(res)
    result = pd.concat(result)
        
    return result
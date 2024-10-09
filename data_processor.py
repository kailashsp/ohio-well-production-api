import pandas as pd
import requests
import io


def read_url(url:str ="https://ohiodnr.gov/static/documents/oil-gas/production/20210309_2020_1%20-%204.xls") -> pd.DataFrame:
    response = requests.get(url)
    print(response)
    df = pd.read_excel(io.BytesIO(response.content))
    return df

def read_xls(path:str) -> pd.DataFrame:
    df = pd.read_excel(path)
    return df


def compute_annual_data(df:pd.DataFrame):
    annual_data = df.groupby('API WELL  NUMBER').agg({
            'OIL': 'sum',
            'GAS': 'sum',
            'BRINE': 'sum'
        }).reset_index()
    return annual_data

if __name__=="__main__":
    df = read_xls('dataset/production.xls')
    res = compute_annual_data(df)

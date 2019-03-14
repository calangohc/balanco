from datetime import datetime

import pandas as pd


def extract_dataframe(file_path):
    dataframe = pd.DataFrame(
        pd.read_csv(file_path, encoding='utf-8'),
        columns=['Data', 'Nome', 'Líquido']
    )

    dataframe.rename(
        columns={
            'Data': 'data',
            'Nome': 'quem',
            'Líquido': 'valor',
        },
        inplace=True,
    )

    dataframe['data'] = dataframe['data'].apply(format_date)
    dataframe['valor'] = dataframe['valor'].apply(format_value)
    dataframe['origem'] = 'paypal'

    return dataframe[['data', 'quem', 'origem', 'valor']]


def format_date(date):
    return datetime.strptime(str(date), '%d/%m/%Y').strftime('%d/%m/%Y')


def format_value(value):
    return float(value.replace(".", "").replace(",", "."))

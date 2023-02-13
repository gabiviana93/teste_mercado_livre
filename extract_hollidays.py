import requests
import json
import pandas as pd

""" 
Extração de dados da API Calendarific (https://calendarific.com), que traz os feriados e datas comemorativas de mais de 230 países
Deixei por padrão o ano de 2021 e o mês de junho por serem os dados necessários a análise das ofertas relâmpago
"""


class GetHollidays():

    def __init__(self, year='2021', month='6', saveName = "dataset_datas_comem_feriados"):
        self.year = year
        self.month = month
        self.url = f"https://calendarific.com/api/v2/holidays?&api_key=feee37c6c4eab25a4810365d856fdb3bb70d4403&country=BR&year={self.year}&month={self.month}"
        self.saveName = saveName


    def get_holidays(self):
        url = self.url
        response = requests.get(url)
        if response.status_code == 200:
            holidays = json.loads(response.content.decode('utf-8'))
            holiday_list = []
            for holiday in holidays['response']['holidays']:
                df_holiday = {}
                df_holiday["Name"] = holiday['name']
                df_holiday["Date"] = holiday['date']['iso']
                holiday_list.append(df_holiday)

            dataset = pd.DataFrame(holiday_list)
            dataset.to_csv(f"datasets/{self.saveName}.csv", header=True, index=False)
        else:
            return None

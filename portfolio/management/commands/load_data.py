from django.core.management.base import BaseCommand
import pandas as pd
from portfolio.models import Asset, AssetPrice, Portfolio, PortfolioAsset
from datetime import datetime
import os

class Command(BaseCommand):
    help = 'Carga datos desde Excel'

    def handle(self, *args, **kwargs):
        df_weights = pd.read_excel('datos.xlsx', sheet_name='weights')
        df_prices = pd.read_excel('datos.xlsx', sheet_name='Precios')

        for symbol in df_prices.columns[1:]:
            Asset.objects.get_or_create(symbol=symbol, name=symbol)

        for index, row in df_prices.iterrows():
            date = pd.to_datetime(row['Dates']).date()
            for symbol in df_prices.columns[1:]:
                asset = Asset.objects.get(symbol=symbol)
                AssetPrice.objects.update_or_create(
                    asset=asset,
                    date=date,
                    defaults={'price': row[symbol]}
                )

        for col in ['portafolio 1', 'portafolio 2']:
            portfolio, _ = Portfolio.objects.get_or_create(
                name=col, initial_value=1_000_000_000, creation_date=datetime(2022,2,15)
            )
            for _, row in df_weights.iterrows():
                asset = Asset.objects.get(symbol=row['activos'])
                PortfolioAsset.objects.update_or_create(
                    portfolio=portfolio,
                    asset=asset,
                    defaults={'initial_weight': row[col]}
                )

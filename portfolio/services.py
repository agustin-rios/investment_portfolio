from decimal import Decimal
from datetime import date
from .models import Portfolio, PortfolioAsset, AssetPrice

def calculate_initial_quantities(portfolio_name, initial_date=date(2022, 2, 15)):
    portfolio = Portfolio.objects.get(name=portfolio_name)
    assets_in_portfolio = PortfolioAsset.objects.filter(portfolio=portfolio)

    for pa in assets_in_portfolio:
        price = AssetPrice.objects.get(asset=pa.asset, date=initial_date).price
        pa.initial_quantity = (pa.initial_weight * portfolio.initial_value) / price
        pa.save()

    return f"Initial quantities calculated for {portfolio_name}."

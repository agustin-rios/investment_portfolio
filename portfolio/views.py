from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, timedelta
from decimal import Decimal
from .models import Portfolio, PortfolioAsset, AssetPrice
from .serializer import PortfolioHistorySerializer

@api_view(['GET'])
def portfolio_history(request, portfolio_id):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')

    fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d').date()
    fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d').date()

    portfolio = Portfolio.objects.get(id=portfolio_id)
    assets = PortfolioAsset.objects.filter(portfolio=portfolio)

    current_date = fecha_inicio
    history = []

    while current_date <= fecha_fin:
        daily_total = Decimal('0')
        daily_values = {}

        for pa in assets:
            price_qs = AssetPrice.objects.filter(asset=pa.asset, date=current_date)
            if price_qs.exists():
                asset_value = pa.initial_quantity * price_qs.first().price
                daily_values[pa.asset.symbol] = asset_value
                daily_total += asset_value

        daily_weights = {
            symbol: (value / daily_total).quantize(Decimal('0.000001'))
            for symbol, value in daily_values.items()
        }

        history.append({
            'date': current_date,
            'total_value': daily_total.quantize(Decimal('0.0001')),
            'asset_weights': daily_weights
        })

        current_date += timedelta(days=1)

    serializer = PortfolioHistorySerializer(history, many=True)
    return Response(serializer.data)

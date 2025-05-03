from django.contrib import admin
from .models import Asset, Portfolio, AssetPrice, PortfolioAsset

admin.site.register(Asset)
admin.site.register(Portfolio)
admin.site.register(AssetPrice)
admin.site.register(PortfolioAsset)

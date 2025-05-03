from django.db import models

class Asset(models.Model):
    name = models.CharField(max_length=100, unique=True)
    symbol = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.symbol

class Portfolio(models.Model):
    name = models.CharField(max_length=100, unique=True)
    initial_value = models.DecimalField(max_digits=20, decimal_places=2)
    creation_date = models.DateField()

    def __str__(self):
        return self.name

class AssetPrice(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='prices')
    date = models.DateField()
    price = models.DecimalField(max_digits=20, decimal_places=4)

    class Meta:
        unique_together = ('asset', 'date')
        ordering = ['date']

class PortfolioAsset(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='portfolio_assets')
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    initial_weight = models.DecimalField(max_digits=10, decimal_places=6)
    initial_quantity = models.DecimalField(max_digits=20, decimal_places=6, null=True, blank=True)

    class Meta:
        unique_together = ('portfolio', 'asset')

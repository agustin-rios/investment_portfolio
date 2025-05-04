from rest_framework import serializers
from .models import Portfolio, PortfolioAsset, AssetPrice

class AssetPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetPrice
        fields = '__all__'

class PortfolioAssetSerializer(serializers.ModelSerializer):
    asset_prices = AssetPriceSerializer(many=True, read_only=True)

    class Meta:
        model = PortfolioAsset
        fields = ['asset', 'initial_weight', 'initial_quantity', 'asset_prices']
        read_only_fields = ['asset_prices']
        extra_kwargs = {
            'initial_weight': {'required': True},
            'initial_quantity': {'required': False}
        }
        
class PortfolioHistorySerializer(serializers.Serializer):
    date = serializers.DateField()
    total_value = serializers.DecimalField(max_digits=20, decimal_places=4)
    asset_weights = serializers.DictField(child=serializers.DecimalField(max_digits=10, decimal_places=6))

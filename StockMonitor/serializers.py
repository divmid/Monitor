from .models import User, Stock
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'dingding_token', 'is_active', 'create_date')


class StockSerializer(serializers.HyperlinkedModelSerializer):

    create_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    class Meta:
        model = Stock
        fields = ('id', 'user', 'name', 'stock_code', 'max_proportion',
                  'min_proportion', 'polling_interval', 'create_date')




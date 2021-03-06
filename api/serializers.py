from rest_framework import serializers
from api.models import *


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = '__all__'

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        exclude = ('created_at', 'updated_at', 'on_delete')

class TrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRateLog
        fields = ('date_rate', 'rate')

class TrackSerializer(serializers.ModelSerializer):
    from_rate = serializers.ReadOnlyField()
    to_rate = serializers.ReadOnlyField()

    class Meta:
        model = ExchangeRateLog
        fields = '__all__'
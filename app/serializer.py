from rest_framework import serializers
from . models import *


class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['symbol', 'name','actual_price', 'date']
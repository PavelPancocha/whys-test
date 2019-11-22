from rest_framework import serializers
from restapp.models import Data


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ["id", "name", "data"]

from rest_framework import serializers
from restapp.models import AttributeName


class AttributeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeName
        fields = ["id", "name"]
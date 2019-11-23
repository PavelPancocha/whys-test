from rest_framework import serializers
from restapp.models import AttributeName


class AttributeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeName
        fields = ["id", "name"]

        #  https://stackoverflow.com/questions/45389188/customize-json-response-in-django-rest-framework
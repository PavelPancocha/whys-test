from rest_framework import serializers
from restapp.models import Data


class DataSerializer(serializers.BaseSerializer):
    def to_internal_value(self, data):
        values = dict()
        for k, v in data.items():
            name = k
            eid = v["id"]
            data = v
            values = {"name": name, "eid": eid, "data": data}
        return values

    def create(self, validated_data):
        try:
            item = Data.objects.get(name=validated_data["name"], eid=validated_data["eid"])
            old_data = eval(item.data)
            new_data = validated_data["data"]
            old_data.update(new_data)
            validated_data["data"] = old_data
        except Data.DoesNotExist:
            pass
        return Data.objects.update_or_create(**validated_data)

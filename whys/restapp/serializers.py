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
            print("validated_data: ", validated_data["name"], validated_data["eid"])
            item = Data.objects.get(name=validated_data["name"], eid=validated_data["eid"])
            print("try item: ", item)
            old_data = eval(item.data)
            print(old_data)
            new_data = validated_data["data"]
            old_data.update(new_data)
            validated_data["data"] = old_data
        except Data.DoesNotExist:
            pass
        except Data.MultipleObjectsReturned:  # this error shouldnt be possible if everything works
            print("this should not happened")
            data = Data.objects.filter(name=validated_data["name"], eid=validated_data["eid"])
            print(data)
        return Data.objects.update_or_create(name=validated_data["name"], eid=validated_data["eid"],
                                             defaults={'data': validated_data["data"]})

    def to_representation(self, instance):  # list representation
        name = instance.name
        eid = int(instance.eid)
        representation = {name: {"id": eid}}
        return representation

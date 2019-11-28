from rest_framework import serializers
from restapp.models import AttributeName, Data


class AttributeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeName
        fields = ["id", "name"]


class DataSerializer(serializers.BaseSerializer):
    def to_internal_value(self, data):
        print("I am from to internal value", data)
        values = dict()
        for k, v in data.items():
            print("I am key", k)
            name = k
            eid = v["id"]
            data = v
            values = {"name": name, "eid": eid, "data": data}
        print("I am value: ", values)
        return values

    def create(self, validated_data):
        try:
            item = Data.objects.get(name=validated_data["name"], eid=validated_data["eid"])
            print("validated data from try: ", validated_data, type(validated_data))
            print("item: ", item, type(item))
            old_data = eval(item.data)
            new_data = validated_data["data"]

            print("From try,: ", old_data, type(old_data))
            old_data.update(new_data)
            validated_data["data"] = old_data
        except Data.DoesNotExist:
            pass
        return Data.objects.create(**validated_data)




        #  https://stackoverflow.com/questions/45389188/customize-json-response-in-django-rest-framework
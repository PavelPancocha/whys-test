from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from restapp.models import AttributeName
from restapp.serializers import AttributeNameSerializer


@csrf_exempt
def attribute_name_list(request):
    if request.method == "GET":
        data_objects = AttributeName.objects.all()
        serializer = AttributeNameSerializer(data_objects, many=True)
        print(serializer)
        return JsonResponse(serializer.data, safe=False)

#  https://stackoverflow.com/questions/45389188/customize-json-response-in-django-rest-framework
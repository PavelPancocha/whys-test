from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from restapp.models import Data
from restapp.serializers import DataSerializer


# @csrf_exempt
# def attribute_name_list(request):
#     if request.method == "GET":
#         data_objects = AttributeName.objects.all()
#         serializer = AttributeNameSerializer(data_objects, many=True)
#         print(serializer)
#         return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def import_end_point(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = DataSerializer(data=data, many = True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data, safe=False, status=201)
        return JsonResponse(status=400)

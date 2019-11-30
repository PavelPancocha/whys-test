from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from restapp.models import Data
from restapp.serializers import DataSerializer, DataDetailSerializer
from rest_framework.exceptions import ParseError


@csrf_exempt
def import_end_point(request):
    """
    Import point. Accepting anything in this format:
    [
    {"Name": {"id": 1,"anyOtherData": 1}
    }
    ]
    Name and ID are required!
    """
    if request.method == "POST":
        try:
            data = JSONParser().parse(request)
            serializer = DataSerializer(data=data, many=True)
            serializer.is_valid()
        except KeyError:
            return JsonResponse("Not correct data. Name, ID fields are required!", safe=False, status=400)
        except ParseError:
            return JsonResponse("Wrong data format. Parsing error.", safe=False, status=400)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status=201)
        return JsonResponse("not valid data", safe=False, status=400)


@csrf_exempt
def list_data_view(request, name):
    if request.method == "GET":
        data = Data.objects.filter(name__iexact=name)
        if data:
            serializer = DataSerializer(data, many=True)
            return JsonResponse(serializer.data, safe=False, status=200)
        else:
            return JsonResponse("Does not exist. Really. I looked twice!", safe=False, status=404)
    else:
        return JsonResponse("Accepting just GET", safe=False, status=400)


@csrf_exempt
def detail_data_view(request, name, eid):
    if request.method == "GET":
        print("got here", name, eid)
        data = Data.objects.filter(name__iexact=name, eid=eid)
        print("__data__", data)
        if data:
            serializer = DataDetailSerializer(data[0], many=False)
            print("serializer data", type(serializer.data), serializer.data)
            return JsonResponse(serializer.data, safe=True, status=200)
        else:
            return JsonResponse("Does not exist. Really. I looked twice!", safe=False, status=404)
    else:
        return JsonResponse("Accepting just GET", safe=False, status=400)


# TODO all view
@csrf_exempt
def all_data_view(request):
    if request.method == "GET":
        data = Data.objects.all()
        if data:
            serializer = DataSerializer(data, many=True)
            return JsonResponse(serializer.data, safe=False, status=200)
        else:
            return JsonResponse("Does not exist. Really. I looked twice!", safe=False, status=404)
    else:
        return JsonResponse("Accepting just GET", safe=False, status=400)
# TODO authentication

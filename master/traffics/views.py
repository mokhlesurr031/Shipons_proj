from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import TrafficData, TrafficTimeStamp
from .serializers import TrafficDataSerializer, TrafficTimeStampSerializer

# Create your views here.


def index(request):
    traffic = TrafficData.objects.all()
    serializer = TrafficDataSerializer(traffic, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def traffic_timestamp(request):
    tt = TrafficTimeStamp.objects.all()
    print("TT", tt)
    serializer = TrafficTimeStampSerializer(tt, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def traffic_timestamp_by_cam(request, cam_id):
    print(cam_id)
    all_data = TrafficData.objects.filter(cam_id = cam_id)
    serializer = TrafficDataSerializer(all_data, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def traffic_timestamp_by_cam_id_id(request, cam_id, entry_id):
    all_data = TrafficTimeStamp.objects.filter(traffic_id=entry_id)
    serializer = TrafficTimeStampSerializer(all_data, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def all_data_by_license_plate(request, license):
    pass





@csrf_exempt
def traffic_data(request):
    if request.method == 'GET':
        return HttpResponse("Traffic Data")

    if request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        if data['license_plate'] != "":
            try:
                data_id = TrafficData.objects.get(license_plate = data['license_plate'], cam_id = data['cam_id'])
                print(data_id.id)
                data_id.count += 1
                data_id.save()
                traffic_timestamp = {'traffic_id': data_id.id}
                tt_serializer = TrafficTimeStampSerializer(data=traffic_timestamp)
                if tt_serializer.is_valid():
                    tt_serializer.save()
            except:
                print("No Data")
                serializer = TrafficDataSerializer(data=data)
                if serializer.is_valid():
                    traffic_id = serializer.save()
                    traffic_timestamp = {'traffic_id': traffic_id.id}
                    tt_serializer = TrafficTimeStampSerializer(data=traffic_timestamp)
                    if tt_serializer.is_valid():
                        tt_serializer.save()

                    return JsonResponse(serializer.data, status=201)
                return JsonResponse(serializer.errors, status=400)

        else:
            try:
                div_id = TrafficData.objects.get(cam_id=data['cam_id'], license_plate = "Unrecognized")
                div_id.count +=1
                div_id.save()
                traffic_timestamp = {'traffic_id': div_id.id}
                tt_serializer = TrafficTimeStampSerializer(data=traffic_timestamp)
                if tt_serializer.is_valid():
                    tt_serializer.save()
            except:
                empty_data = {'license_plate': 'Unrecognized', 'cam_id': data['cam_id']}
                serializer = TrafficDataSerializer(data=empty_data)
                if serializer.is_valid():
                    traffic_id = serializer.save()
                    traffic_timestamp = {'traffic_id': traffic_id.id}
                    tt_serializer = TrafficTimeStampSerializer(data=traffic_timestamp)
                    if tt_serializer.is_valid():
                        tt_serializer.save()
                    return JsonResponse(serializer.data, status=201)
                return JsonResponse(serializer.errors, status=400)






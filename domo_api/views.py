from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from domo_api.models import *
from domo_api.serializers import *


class Locations_method(APIView):
    def post(self, request):
        name_location = request.data["name_location"]      
        user = request.data["user_id"]
        locations = Locations.objects.create(name_location=name_location, user_id=user)
        return Response(status=status.HTTP_200_OK)
    
    def put(self, request, codigo):
        location=Locations.objects.get(id=codigo)
        location.name_location = request.data["name_location"]      
        location.save()
        return Response(status=status.HTTP_200_OK)

    def get(self, request, codigo):
        locations = Locations.objects.filter(user_id = codigo)
        content = {}
        locations_list = LocationSerializers(locations,many=True).data
        content["locations"] = locations_list
        return Response(content, status=status.HTTP_200_OK)
    
    def delete(self, request, codigo):
        location=Locations.objects.get(id=codigo)
        location.delete()
        return Response(status=status.HTTP_200_OK)
    


class Devices_method(APIView):
    def post(self, request):
        name_devices = request.data["name_device"]     
        unit = request.data["unit"] 
        location = request.data["location_id"]
        devices = Devices.objects.create(name_device=name_devices,unit=unit, location_id=location)
        return Response(status=status.HTTP_200_OK)
    
    def put(self, request, codigo):
        device=Devices.objects.get(id=codigo)
        device.name_device = request.data["name_device"]      
        device.save()
        return Response(status=status.HTTP_200_OK)

    def get(self, request, codigo):
        devices = Devices.objects.filter(user_id = codigo)
        content = {}
        devices_list = DeviceSerializers(devices,many=True).data
        content["devices"] = devices_list
        return Response(content, status=status.HTTP_200_OK)
    
    def delete(self, request, codigo):
        device=Devices.objects.get(id=codigo)
        device.delete()
        return Response(status=status.HTTP_200_OK)
    
class Dots_method(APIView):
    def post(self, request):
        value = request.data["value"]     
        dateTime = request.data["dateTime"] 
        device = request.data["device_id"]
        devices = Devices.objects.create(value=value,dateTime=dateTime, device_id=device)
        return Response(status=status.HTTP_200_OK)
    
    def put(self, request, codigo):
        dot=Dots.objects.get(id=codigo)
        dot.value = request.data["value"]      
        dot.save()
        return Response(status=status.HTTP_200_OK)

    def get(self, request, codigo):
        dots = Dots.objects.filter(user_id = codigo)
        content = {}
        dots_list = DotSerializers(dots,many=True).data
        content["dots"] = dots_list
        return Response(content, status=status.HTTP_200_OK)
    
    def delete(self, request, codigo):
        dot=Dots.objects.get(id=codigo)
        dot.delete()
        return Response(status=status.HTTP_200_OK)

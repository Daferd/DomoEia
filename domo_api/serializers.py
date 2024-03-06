from rest_framework import serializers

class LocationSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    name_location = serializers.CharField(max_length=255)
    user_id = serializers.IntegerField()

class DeviceSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    name_device = serializers.CharField(max_length=255)
    unit = serializers.CharField(max_length=255)
    location_id = serializers.IntegerField()

class DotSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    value = serializers.FloatField()
    dateTime = serializers.DateTimeField()
    device_id = serializers.IntegerField()


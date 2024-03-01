from rest_framework import serializers

class LocationSerializers(serializers.Serializer):
    name_location = serializers.CharField(max_length=255)
    user_id = serializers.IntegerField()

class DeviceSerializers(serializers.Serializer):
    name_device = serializers.CharField(max_length=255)
    unit = serializers.CharField(max_length=255)
    locations = serializers.IntegerField()

class DotSerializers(serializers.Serializer):
    value = serializers.FloatField()
    dateTime = serializers.DateTimeField()
    device = serializers.IntegerField()


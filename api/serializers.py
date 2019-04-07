from rest_framework import serializers
from api.models import SpaceSignal


class SignalSerializer(serializers.Serializer):
    system = serializers.CharField(max_length=50)
    publish_date = serializers.DateTimeField(required=False)
    author = serializers.CharField(max_length=50)
    content = serializers.CharField(max_length=140)

    def create(self, validated_data):
        return SpaceSignal.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.system = validated_data.get('system', instance.system)
        instance.created_date = validated_data.get('created_date', instance.created_date)
        instance.publish_date = validated_data.get('publish_date', instance.publish_date)
        instance.author = validated_data.get('author', instance.author)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance

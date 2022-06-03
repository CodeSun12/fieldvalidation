from .models import Squad
from rest_framework import serializers


class SquadSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    members = serializers.IntegerField()
    color = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Squad.objects.create(**validated_data)

    # TODO FIELD LEVEL VALIDATION
    def validate_members(self, value):
        if value >= 12:
            raise serializers.ValidationError("Members should be 11 only")
        return value

    # TODO OBJECT LEVEL VALIDATION
    def validate(self, data):
        nm = data.get('name')
        clr = data.get('color')
        if nm.lower() != 'k' and clr.lower() != 'combination of blue and black':
            raise serializers.ValidationError("Name should be start with k and color must be combination of blue and black")
        return data

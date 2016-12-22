from rest_framework import serializers
from search.models import Zapisek

class ZapisekSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    naslov = serializers.CharField(max_length=50)
    besedilo = serializers.CharField(max_length=1000)
    

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Zapisek.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.naslov = validated_data.get('naslov', instance.naslov)
        instance.besedilo = validated_data.get('besedilo', instance.besedilo)
        
        instance.save()
        return instance
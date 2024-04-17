from rest_framework import serializers
from .models import Room

#This serializer class take the model Room and take python related
#code and translate into json response

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause', 
                  'votes_to_skip', 'created_at')
        


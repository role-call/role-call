from django.contrib.auth.models import User, Group
from rest_framework import serializers
from attendance.models import Occupant, Installation, Facility,Occupant_Picture

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class Occupant_PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupant_Picture
        fields = ['external_id','imageType','img','modified_at']

class OccupantSerializer(serializers.ModelSerializer):
    picture = Occupant_PictureSerializer(read_only=True, many=True)
    # picture = serializers.CharField()
    class Meta:
        model = Occupant
        lookup_field = 'external_id'
        extra_kwargs = {
            'url': {'lookup_field': 'external_id'}
        }

        fields = ['external_id', 'firstName', 'lastName','picture', 'created_at', 'deleted_at']


class FacilitySerializer(serializers.ModelSerializer):
    occupant = OccupantSerializer(read_only=True, many=True)
    class Meta:
        model = Facility
        lookup_field = 'external_id'
        fields = ['external_id','occupant', 'name','installation']
class InstallationSerializer(serializers.ModelSerializer):
    facility = FacilitySerializer(read_only=True, many=True)
    class Meta:
        model = Installation
        lookup_field = 'external_id'
        fields = ['external_id', 'name', 'prefs', 'facility']
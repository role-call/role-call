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

class Occupant_PictureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Occupant_Picture
        fields = ['external_id','img','modified_at']

class OccupantSerializer(serializers.HyperlinkedModelSerializer):
    picture = Occupant_PictureSerializer(read_only=True)
    class Meta:
        model = Occupant
        lookup_field = 'external_id'
        extra_kwargs = {
            'url': {'lookup_field': 'external_id'}
        }

        fields = ['external_id', 'firstName', 'lastName','picture', 'created_at', 'deleted_at']

class InstallationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Installation
        fields = ['external_id', 'name','prefs']
class FacilitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Facility
        fields = ['external_id', 'name','installation']

from rest_framework import serializers
from .models import Profile, Housing

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['url', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Profile(**validated_data)
        user.set_password(password)
        user.save()
        return user

class HousingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Housing
        fields = ['url', 'house_id', 'city', 'street', 'street_number', 'floor', 'door', 'house_dimension', 'house_owner', 'image']
        

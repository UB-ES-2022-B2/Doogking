from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import Profile, Housing
from django.contrib.auth.models import User

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['url', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}, 'otp':{'read_only':True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Profile(**validated_data)
        user.set_password(password)
        user.save()
        return user

class CurrentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'email', 'first_name', 'last_name']

class HousingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Housing
        fields = ['url', 'house_id', 'city', 'street', 'street_number', 'floor', 'door', 'house_dimension', 'house_owner', 'house_owner_name', 'price', 'rating', 'image']
        
class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)
    #email = serializers.EmailField('email address', unique=True)

    class Meta:
        model = Profile
        fields = ('email','old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance

'''class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)'''

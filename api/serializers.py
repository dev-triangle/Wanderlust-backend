from rest_framework import serializers
from .models import (Place,User,Trending,Stay,UserDetail,Hotel,User,Flight,Review,Train,Travel,Booking,ThingsToDo)
from rest_framework.permissions import IsAuthenticated

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=68,min_length=6,write_only=True)
    permission_classes=[IsAuthenticated]
    class Meta:
        model=User
        fields=['email','username','password','id']

    def validate(self,attrs):
        email=attrs.get('email','')
        username=attrs.get('username','')

        if not username.isalnum():
            raise serializers.ValidationError("username should contain only alpha numeric chars")
        return attrs

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class UserDetailSerializer(serializers.ModelSerializer):
    user_image=serializers.ImageField(max_length=None,allow_empty_file=False,use_url=True,required=False)
    class Meta:
        model=UserDetail
        fields='__all__'

class HotelSerializer(serializers.ModelSerializer):
    hotel_image=serializers.ImageField(max_length=None,allow_empty_file=False,use_url=True,required=False)
    class Meta:
        model=Hotel
        fields='__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email']

class PlaceSerializer(serializers.ModelSerializer):
    place_image=serializers.ImageField(max_length=None,allow_empty_file=False,use_url=True,required=False)
    class Meta:
        model=Place
        fields='__all__'

class TrendingSerializer(serializers.ModelSerializer):
    place_image=serializers.ImageField(max_length=None,allow_empty_file=False,use_url=True,required=False)
    class Meta:
        model=Trending
        fields='__all__'

class StaySerializer(serializers.ModelSerializer):
    stay_image=serializers.ImageField(max_length=None,allow_empty_file=False,use_url=True,required=False)
    class Meta:
        model=Stay
        fields='__all__'

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flight
        fields='__all__'

class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model=Train
        fields='__all__'

class TravelSerializer(serializers.ModelSerializer):
    place_image=serializers.ImageField(max_length=None,allow_empty_file=False,use_url=True,required=False)
    class Meta:
        model=Travel
        fields='__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields='__all__'

class ThingsToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model=ThingsToDo
        fields='__all__'
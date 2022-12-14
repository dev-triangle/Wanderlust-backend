from rest_framework import generics,mixins,viewsets,status
from .models import (Place,User,Trending,Stay,UserDetail,Hotel,Flight,Review,Train,Travel,Booking,ThingsToDo)
from .serializers import (PlaceSerializer,UserSerializer,RegisterSerializer,TrendingSerializer,
                        StaySerializer,FlightSerializer,BookingSerializer,
                        UserDetailSerializer,HotelSerializer,ReviewSerializer,TrainSerializer,TravelSerializer,ThingsToDoSerializer)
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,AllowAny
from rest_framework.response import Response
from django.http import HttpResponse
# Create your views here.
class PlaceViewSet(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    queryset=Place.objects.all()
    serializer_class=PlaceSerializer
 
class RegisterView(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    serializer_class=RegisterSerializer
    queryset=User.objects.all()

class TrendingView(viewsets.GenericViewSet,mixins.ListModelMixin):
    serializer_class=TrendingSerializer
    queryset=Trending.objects.all()

class StayView(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    serializer_class=StaySerializer
    queryset=Stay.objects.all()

class ReviewViewset(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=ReviewSerializer
    queryset=Review.objects.all()

class UserViewset(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    serializer_class=UserSerializer
    queryset=User.objects.all()
    
class HotelViewset(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    serializer_class=HotelSerializer
    queryset=Hotel.objects.all()

class UserDetailViewset(viewsets.GenericViewSet,mixins.DestroyModelMixin,mixins.UpdateModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    serializer_class=UserDetailSerializer
    queryset=UserDetail.objects.all()

class FlightDetailViewset(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    serializer_class=FlightSerializer
    queryset=Flight.objects.all()

class TrainDetailViewset(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    serializer_class=TrainSerializer
    queryset=Train.objects.all()

class TravelDetailViewset(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    serializer_class=TravelSerializer
    queryset=Travel.objects.all()


class BookingViewset(viewsets.GenericViewSet,mixins.UpdateModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    permission_classes=[IsAuthenticated]
    serializer_class=BookingSerializer
    queryset=Booking.objects.all()

class ThingsToDoViewSet(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    queryset=ThingsToDo.objects.all()
    serializer_class=ThingsToDoSerializer

class BlacklistTokenView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        try:
            refresh_token=request.data["refresh_token"]
            token=RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class LoggedInUserView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
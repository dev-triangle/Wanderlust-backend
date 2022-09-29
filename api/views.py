from django.shortcuts import render
from rest_framework import generics,mixins,viewsets,status
from .models import Place,User,Trending
from .serializers import PlaceSerializer,UserSerializer,RegisterSerializer,TrendingSerializer
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
# Create your views here.
class PlaceViewSet(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    queryset=Place.objects.all()
    serializer_class=PlaceSerializer

class RegisterView(viewsets.GenericViewSet,mixins.CreateModelMixin):
    serializer_class=RegisterSerializer
    queryset=User.objects.all()

class TrendingView(viewsets.GenericViewSet,mixins.ListModelMixin):
    serializer_class=TrendingSerializer
    queryset=Trending.objects.all()
    
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
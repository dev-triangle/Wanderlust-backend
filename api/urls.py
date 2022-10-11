from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import (BlacklistTokenView,LoggedInUserView,RegisterView,TrendingView,PlaceViewSet,
                    StayView,UserDetailViewset,HotelViewset,UserViewset,FlightDetailViewset,ReviewViewset)
router=DefaultRouter()
router.register('places',PlaceViewSet, basename='places')
router.register('register',RegisterView,basename='register')
router.register('trending',TrendingView,basename='trending')
router.register('stays',StayView,basename='stays')
router.register('user-detail',UserDetailViewset,basename='user-detail')
router.register('hotels',HotelViewset,basename='hotels')
router.register('users',UserViewset,basename='users')
router.register('flights',FlightDetailViewset,basename='flights')
router.register('reviews',ReviewViewset,basename='reviews')

urlpatterns = [
    path('',include(router.urls)),
    path('api/token/',TokenObtainPairView.as_view(),name="token_obtain"),
    path('api/token/refresh/',TokenRefreshView.as_view(),name="refresh_token"),
    path('api/token/blacklist/',BlacklistTokenView.as_view(),name="blacklist"),
    path('current-user/', LoggedInUserView.as_view(), name='currentuser'),
]
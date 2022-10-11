from django.contrib import admin
from .models import (Place,User,Trending,Stay,UserDetail,Hotel)
# Register your models here.
admin.site.register(Place)
admin.site.register(User)
admin.site.register(Trending)
admin.site.register(Stay)
admin.site.register(UserDetail)
admin.site.register(Hotel)
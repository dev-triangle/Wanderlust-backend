from django.contrib import admin
from .models import (Place,User,Trending,Stay,UserDetail,Hotel,Flight,Review,Train,Travel)
# Register your models here.
admin.site.register(Place)
admin.site.register(User)
admin.site.register(Trending)
admin.site.register(Stay)
admin.site.register(UserDetail)
admin.site.register(Hotel)
admin.site.register(Flight)
admin.site.register(Review)
admin.site.register(Train)
admin.site.register(Travel)

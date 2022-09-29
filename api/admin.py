from django.contrib import admin
from .models import Place,User,Trending
# Register your models here.
admin.site.register(Place)
admin.site.register(User)
admin.site.register(Trending)
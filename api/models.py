from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager,PermissionsMixin)
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if username is None:
            raise TypeError("Users should have a username")

        if email is None:
            raise TypeError("Users should have a email")

        user=self.model(username=username,email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,email,password=None):
        if password is None:
            raise TypeError("Password should not be none")
        
        user=self.create_user(username,email,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=255,unique=True,db_index=True)
    email=models.EmailField(max_length=255,unique=True,db_index=True)
    is_verified=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    objects=UserManager()
    def __str__(self):
        return self.username

    def tokens(self):
        return ''

class UserDetail(models.Model):
    user_foreign=models.ForeignKey(User,on_delete=models.CASCADE)
    actual_name=models.CharField(max_length=200,blank=True,null=True)
    phno=models.CharField(max_length=10,blank=True,null=True)
    user_image=models.ImageField(upload_to='user_images',blank=True,null=True)
    def __str__(self):
        return(self.actual_name)

class Place(models.Model):
    place_name=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    place_image=models.ImageField(upload_to='place_images',blank=True,null=True)
    place_desc=models.TextField(max_length=1000)
    def __str__(self):
        return (self.place_name)

class Travel(models.Model):
    place_foreign=models.ForeignKey(Place,on_delete=models.CASCADE)
    vehicle_name=models.CharField(max_length=100)
    passenger_max=models.IntegerField()
    place_image=models.ImageField(upload_to='vehicle_images',blank=True,null=True)

    def __str__(self):
        return (self.vehicle_name)

class Hotel(models.Model):
    place_foreign=models.ForeignKey(Place,on_delete=models.CASCADE)
    hotel_name=models.CharField(max_length=200)
    near_point=models.CharField(max_length=300)
    hotel_image=models.ImageField(upload_to='hotel_images',blank=True,null=True)
    famous_foods=models.CharField(max_length=500)

    def __str__(self):
        return(self.hotel_name)

class Review(models.Model):
    place_foreign=models.ForeignKey(Place,on_delete=models.CASCADE)
    user_foreign=models.ForeignKey(User,on_delete=models.CASCADE)
    desc=models.TextField(max_length=500)
    rate=models.IntegerField()

    def __int__(self):
        return(self.place_foreign)

class Trending(models.Model):
    place_name=models.CharField(max_length=100)
    place_image=models.ImageField(upload_to='trending_images',blank=True,null=True)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    photographer_name=models.CharField(max_length=100)

    def __str__(self):
        return(self.place_name)

class Stay(models.Model):
    place_foreign=models.ForeignKey(Place,on_delete=models.CASCADE)
    stay_name=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    stay_image=models.ImageField(upload_to='stay_images',blank=True,null=True)

    def __str__(self):
        return(self.stay_name)

class Flight(models.Model):
    to_place_foreign=models.ForeignKey(Place,on_delete=models.CASCADE)
    flight_name=models.CharField(max_length=100)
    cost=models.FloatField()
    flight_time=models.TimeField()
    next_date=models.DateField()

    def __str__(self):
        return(self.flight_name)

class Train(models.Model):
    to_place_foreign=models.ForeignKey(Place,on_delete=models.CASCADE)
    train_name=models.CharField(max_length=100)
    cost=models.FloatField()

    def __str__(self):
        return(self.train_name)

class Booking(models.Model):
    user_foreign=models.ForeignKey(User,on_delete=models.CASCADE)
    place_foreign=models.ForeignKey(Place,on_delete=models.CASCADE)
    stay_foreign=models.ForeignKey(Stay,on_delete=models.CASCADE)
    travel_foreign=models.ForeignKey(Travel,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booking_status=models.BooleanField(default=False)
    
    def __int__(self):
        return(self.id)



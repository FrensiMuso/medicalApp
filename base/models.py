from django.db import models
from django.contrib.auth.models import AbstractUser

#Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    role = models.CharField(max_length=100, default="patient")
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class TemperatureData(models.Model):
    patient = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    value = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)#set time everytime is saved
    created = models.DateTimeField(auto_now_add=True)#when we first save it, it never changes
    # class Meta:
    #     ordering = ['-updated', '-created']

    def __str__(self):
        return str(self.value)
    
class RespirationData(models.Model):
    patient = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    value = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)#set time everytime is saved
    created = models.DateTimeField(auto_now_add=True)#when we first save it, it never changes
    # class Meta:
    #     ordering = [ '-created']
    def __str__(self):
        return str(self.value)
    
class PulseData(models.Model):
    patient = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    value = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)#set time everytime is saved
    created = models.DateTimeField(auto_now_add=True)#when we first save it, it never changes
    # class Meta:
    #     ordering = [ '-created']
    def __str__(self):
        return str(self.value)
    
class HumidityData(models.Model):
    patient = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    value = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)#set time everytime is saved
    created = models.DateTimeField(auto_now_add=True)#when we first save it, it never changes
    # class Meta:
    #     ordering = [ '-created']
    def __str__(self):
        return str(self.value)
    
class SPO2Data(models.Model):
    patient = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    value = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)#set time everytime is saved
    created = models.DateTimeField(auto_now_add=True)#when we first save it, it never changes
    # class Meta:
    #     ordering = [ '-created']
    def __str__(self):
        return str(self.value)
    

class NIBPData(models.Model):
    patient = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    value = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)#set time everytime is saved
    created = models.DateTimeField(auto_now_add=True)#when we first save it, it never changes
    # class Meta:
    #     ordering = [ '-created']
    def __str__(self):
        return str(self.value)
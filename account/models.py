from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # primary_key=True를 해놓으면 새로운 pk가 생성되지 않는다.
    username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True) 
    email = models.EmailField(max_length=100, blank=True)
    introduction = models.CharField(max_length=200, blank=True)

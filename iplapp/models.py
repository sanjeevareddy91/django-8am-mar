from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# name,nickname,team_logo,captain_name,started_year

class Team_Name(models.Model):
    team_name = models.CharField(max_length=30)
    nick_name = models.CharField(max_length=5)
    team_logo = models.ImageField(upload_to='logos',null=True,blank=True)
    captain_name = models.CharField(max_length=30)
    started_year = models.IntegerField()

    def __str__(self) -> str:
        return self.team_name
    class Meta:
        db_table = 'team_name'

class UserInfo(models.Model):
    user_data = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=10)
    verify_code = models.CharField(max_length=7,null=True,blank=True)

    def __str__(self) -> str:
        return self.user_data.username
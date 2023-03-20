from django.db import models

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
from rest_framework import serializers

from .models import Team_Name

class TeamNameModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team_Name
        fields = "__all__"
